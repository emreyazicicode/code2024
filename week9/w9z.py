import matplotlib.pyplot as plt

from sklearn.ensemble import AdaBoostRegressor
from sklearn import datasets, ensemble
import sys
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn import datasets, linear_model

f = "w9_car_price_prediction.csv"
target = "Price"

import pandas as pd 
df = pd.read_csv(f)

df = df[ df['Price'] < 100000 ]
df = df[ df['Price'] > 1500 ]


df = pd.get_dummies( df, columns = ['Airbags'] )


for c in df:
    if 'Airbags' in c:
        print(c, df[ df[c] == 1 ][target].mean())



#MEAN = df[target].mean()
#df[target] = df[target] - MEAN


df['Mileage'] = df['Mileage'].apply(lambda value: int(str(value).replace(" km", "")))

df = df[ df['Mileage'] < df['Mileage'].quantile(0.85) ]
df = df[ df['Prod. year'] > 1990]
df['NEW2012'] = df['Prod. year'] >= 2012


df['Leather interior'] = df['Leather interior'].map({'Yes': 1, 'No': 0})
df['Wheel'] = df['Wheel'].map({'Left wheel': 1, 'Right-hand drive': 0})

df['Doors'] = df['Doors'].map({'04-May': 1, '02-Mar': 0, '>5': 0, None: 1})
df['Doors'] = df['Doors'].fillna(1)
df['Doors'] = df['Doors'].astype(int)


df = pd.get_dummies( df, columns = ['Category'])
df = pd.get_dummies( df, columns = ['Fuel type'])
df = pd.get_dummies( df, columns = ['Gear box type'])
df = pd.get_dummies( df, columns = ['Drive wheels'])



#! BUSINESS DEPARTMENT
#! I have completed the model
#! This model only works for cars whose price is in the range of [1000, 100000]

def fillLevy( row ):
    if row['Levy'] == '-':
        return row['Price'] * 0.107
    else:
        return int(row['Levy'])

df['Levy'] = df.apply( lambda row: fillLevy(row), axis = 1)









def merger( row ):
    if row['Fuel type_Hydrogen'] == 1 and row['Category_Pickup'] == 1: return 1
    else: return 0


df['merged1'] = df.apply(lambda row: merger(row), axis = 1)

#avg = df.groupby(by = ['Model']).agg({target: 'mean'}).to_dict()[target]
#df['BASE'] = df['Model'].map(avg)
#print(df['BASE'].corr(df[target]))


#! BASE PRICE = if a model occoured more than 100 times, get the average price of "model"
#!              else get the average price of "manifacturer"


del df['Fuel type_Hydrogen']
del df['Category_Limousine']
del df['Category_Pickup']
del df['Category_Cabriolet']


"""
df = df.select_dtypes(exclude = ['object'])

for c in df:
    if df[c].nunique() == 2:

        clf0 = RandomForestRegressor(max_depth=5, random_state=0)
        clf1 = RandomForestRegressor(max_depth=5, random_state=0)

        df0 = df[ df[c] == 0 ]
        df1 = df[ df[c] == 1 ]

        limit0 = int(len(df0) * 0.70)
        train0 = df0[:limit0]
        test0 = df0[limit0:]



        clf0.fit( df0.drop(columns=[target]), df0[target] )
        clf1.fit( df1.drop(columns=[target]), df1[target] )

        s0 = clf0.score( df0.drop(columns = [target]), df0[target] )
        s1 = clf1.score( df1.drop(columns = [target]), df1[target] )

        print(c, s0, len(df0), s1, len(df1), (s0 * len(df0) + s1 * len(df1)) / len(df))
"""




"""

def fm1( row ):
    if row['Drive wheels_4x4'] == 1:
        return 1
    if row['Gear box type_Automatic'] == 1:
        return 1
    return 0


df['fm1'] = df.apply(fm1, axis = 1)

print(df['fm1'].corr( df[target] ))
"""




df = df.select_dtypes(exclude = ['object'])

# preprocessing
# normalization
# feature mining
# %95 SAME!!!

clf = RandomForestRegressor(max_depth=7, random_state=0)
clf = ensemble.GradientBoostingRegressor()

#clf = linear_model.LinearRegression()

#* Resample data, shuffle
df = df.sample(frac = 1.0)


#* Split into train test dataset
limit = 0.60
limit = int(len(df) * limit)

train = df[:limit]
test = df[limit:]

train = train.sample(frac = 1.0) # Shuffle
print(train.shape)

#* Split vertical, inputs, output
train_X = train.drop( columns = [target])
train_y = train[target]

test_X = test.drop( columns = [target])
test_y = test[target]


clf.fit(train_X, train_y)
print(clf.score( test_X, test_y ))

test_X['tahmin'] = clf.predict( test_X )# + MEAN
test_X['real'] = test_y #+ MEAN

test_X['error'] = test_X['real'] - test_X['tahmin']
test_X['direction'] = np.sign(test_X['error'])
test_X['abserror'] = np.abs(test_X['error'])
test_X['percentage'] = test_X['error'] / test_X['real']
test_X['abspercentage'] = test_X['abserror'] / test_X['real']


test_X['bigerror'] = test_X['abspercentage'] > 1.0 # %100
test_X['bigerror'] = test_X['bigerror'].astype(int)

small = test_X[test_X['bigerror'] == 0]
big = test_X[test_X['bigerror'] == 1]

print(len(small), len(big))
m = min( len(small), len(big) )


print(df.corr())

#c = 'Airbags'
#plt.hist( small[c].sample(n = m), alpha = 0.4 )
#plt.hist( big[c].sample(n = m), alpha = 0.4 )
#plt.show()


"""
sub = test_X.sample(n = 100)

plt.plot(sub['real'].values)
plt.plot(sub['tahmin'].values)
#plt.hist(test_X['real'], alpha = 0.3)
#plt.hist(test_X['tahmin'], alpha= 0.3)
plt.show()

test_X.to_csv("w9z.csv")

"""