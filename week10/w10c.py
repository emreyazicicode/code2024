import datetime
import pandas as pd
df = pd.read_csv("w10_raw_sales.csv")

#* How many houses will be sold every single day
sales = df['datesold'].value_counts().to_dict()

#* Convert this column into datetime
df['datesold'] = pd.to_datetime(df['datesold'])
#* Find the minimum date
base = df['datesold'].min()
#* Find the RANGE between max and min
numdays = df['datesold'].max() - df['datesold'].min()
#* Convert from DATE SPAN / DATE RANGE to .days (as integer)
numdays = numdays.days
#* Create a list of days
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]

dx = pd.DataFrame(columns = ['date', 'nofsales'])

for d in date_list:
    dx.loc[ len(dx) ] = [d, len(df[ df['datesold'] == d ])]




import matplotlib.pyplot as plt

data = list(dx['nofsales'].values)
data = data[-365:] # last 365
plt.plot( data )
plt.show()



"""
dx = pd.DataFrame(columns = ['date', 'nofsales'])
for s in sales:
    dx.loc[ len(dx) ] = [s, sales[s]]

dx['date'] = pd.to_datetime(dx['date'])
dx = dx.sort_values( by = ['date'])

print(dx)

import matplotlib.pyplot as plt

data = list(dx['nofsales'].values)
data = data[-365:] # last 365
plt.plot( data )
plt.show()

"""
