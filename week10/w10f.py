import sys
import pandas as pd

import holidays
az_holidays = holidays.US()  # this is a dict


f = "w10_trend.csv"
target = 'detrend'

f = 'w10_timeseries.csv'
target = 'nofsales'

df = pd.read_csv(f)
# NOTE, we are only focusing on last years, because if we go back too far, 
# the estimation may be effected by long term effects
# Focus on last part of the data, which is more up-to-date, YENI

#! Auto Correlation = Find the maximum correlated day (lag)
#* One Day Before
lst = []
#* Creating lag based variables
#* 1 year is a long period, which causes two problems
#* First, in one year (long period) there may be other effecting factors
#* Second, we may need to discard 1 year of data because of nulls
for i in range(1, 120):
    #* Try for 365 days
    df[f'L{i}'] = df[target].shift(i) #* Shift = Lag, the value in the same column, i row before
    #* Add to list for displaying only
    lst.append( df[f'L{i}'].corr( df[target] ) )
    #* If it is not a good correlation
    if df[f'L{i}'].corr( df[target] ) < 0.60:
        #* Delete it
        del df[f'L{i}']

import matplotlib.pyplot as plt
plt.plot(lst)
#plt.show()


#! Moving Average
#* Try to create a variable of MOVING averages
for i in range(2, 30+1):
    #* Create the variable
    df[f'MA{i}'] = (df[target].rolling(i).sum() - df[target]) / i

    #* If it is not a good correlation
    if df[f'MA{i}'].corr( df[target] ) < 0.60:
        #* Delete it
        del df[f'MA{i}']


#! Holidays
df['holiday'] = df['date'].apply(lambda value: value in az_holidays)
df['holiday'] = df['holiday'].astype(int)

#! Date-Time related
df['date'] = pd.to_datetime(df['date'])
df['day'] = df['date'].dt.day
df['weekday'] = df['date'].dt.weekday
df['month'] = df['date'].dt.month
df['weekend'] = df['weekday'].isin([5,6]) #* Saturday, Sunday, |monday = 0

season = {
    1: 'winter',
    2: 'winter',
    3: 'spring',
    4: 'spring',
    5: 'spring',
    6: 'summer',
    7: 'summer',
    8: 'summer',
    9: 'autumn',
    10: 'autumn',
    11: 'autumn',
    12: 'winter',
}

quarter = {
    1: 'q1',
    2: 'q1',
    3: 'q1',
    4: 'q2',
    5: 'q2',
    6: 'q2',
    7: 'q3',
    8: 'q3',
    9: 'q3',
    10: 'q4',
    11: 'q4',
    12: 'q4',
}

# summer - winter
sumwin = {
    1: 'w',
    2: 'w',
    3: 'w',
    4: 's',
    5: 's',
    6: 's',
    7: 's',
    8: 's',
    9: 's',
    10: 's',
    11: 'w',
    12: 'w',
}

#! call center, call count estimation, shopping
df['firstdays'] = df['day'] < 7
df['lastdays'] = df['day'] > 24
df['middledays'] = df['day'].isin([12,13,14,15,16,17,18,19])
df['season'] = df['month'].map( season )
df['quarter'] = df['month'].map(quarter )
df['sumwin'] = df['month'].map(sumwin )

df['odd'] = df['weekday'].apply(lambda value: value % 2)

df['December'] = df['month'] == 12

#* 0 monday
#* 2 wednesday
#* 4 friday
#* 6 sunday

#* 1 tuesday
#* 3 thursday
#* 5 saturday

df = pd.get_dummies( df, columns = ['season'] )
df = pd.get_dummies( df, columns = ['quarter'] )
df = pd.get_dummies( df, columns = ['sumwin'] )

print('Weekend', df['weekend'].corr(df[target]))
print('firstdays', df['firstdays'].corr(df[target]))
print('lastdays', df['lastdays'].corr(df[target]))
print('middledays', df['middledays'].corr(df[target]))

print('autumn', df['season_autumn'].corr(df[target]))
print('spring', df['season_spring'].corr(df[target]))
print('summer', df['season_summer'].corr(df[target]))
print('winter', df['season_winter'].corr(df[target]))

print('q1', df['quarter_q1'].corr(df[target]))
print('q2', df['quarter_q2'].corr(df[target]))
print('q3', df['quarter_q3'].corr(df[target]))
print('q4', df['quarter_q4'].corr(df[target]))

print('w', df['sumwin_w'].corr(df[target]))
print('s', df['sumwin_s'].corr(df[target]))

print('odd/even', df['odd'].corr(df[target]))


if 'Unnamed: 0' in df:
    del df['Unnamed: 0']

#* To eliminate "NaN"s, we need to drop na
df = df.dropna()

df = df.tail(4 * 365)

import datetime
from math import ceil

def weekOfMonth(date_time_obj: datetime) -> int:
    first_day = date_time_obj.replace(day=1)
    dom = date_time_obj.day
    adjusted_dom = dom + first_day.weekday()
    return int(ceil(adjusted_dom/7.0))


df['week'] = df['date'].apply(weekOfMonth)


monthly_avg =df.groupby(by = ['month']).agg({target: 'mean'}).to_dict()[target]
weekdaily_avg =df.groupby(by = ['weekday']).agg({target: 'mean'}).to_dict()[target]
daily_avg =df.groupby(by = ['day']).agg({target: 'mean'}).to_dict()[target]
weekly_avg =df.groupby(by = ['week']).agg({target: 'mean'}).to_dict()[target]


df['montlyaverage'] = df['month'].map( monthly_avg )
df['weekdailyaverage'] = df['weekday'].map( weekdaily_avg )
df['dailyaverage'] = df['day'].map( weekdaily_avg )
df['weeklyaverage'] = df['week'].map( weekdaily_avg )


df = df.dropna()

from sklearn.ensemble import RandomForestRegressor

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg = RandomForestRegressor(max_depth=5, random_state=0)
y = df['nofsales']
x = df.drop(columns = ['date', 'nofsales'])
reg.fit( x, y )
df['predict'] = reg.predict(x)


def fix( value ):
    if value < 0: return 0
    return round(value)

df['predict'] = df['predict'].apply(fix)
df['error'] = df[target] - df['predict']
df['abserror'] = df['error'].abs()
df['ape'] = 2 * df['abserror'] / (df['predict'] + df[target] + 0.00001) # NOTE, we add 0.00001 to avoid diving by zero error

df.to_csv("w10_many.csv")


print(df[target].corr(df['predict']))
