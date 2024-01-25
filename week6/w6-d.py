import sys
import matplotlib.pyplot as plt
import pandas as pd

path = "w6_202010-divvy-tripdata.csv"

df = pd.read_csv(path)

print(df.columns)

"""
'ride_id', 
'rideable_type', 
'started_at', 'ended_at',
'start_station_name', 'start_station_id', 
'end_station_name','end_station_id', 
'start_lat', 'start_lng', 
'end_lat', 'end_lng',
'member_casual' = member/casual
"""

df['started_at'] = pd.to_datetime(df['started_at'])
df['ended_at'] = pd.to_datetime(df['ended_at'])

#= Difference between two dates are called "TIME SPAN"
#! df['duration'] = (df['ended_at'] - df['started_at'])


# axis = 1 HORIZONTAL, ROW BY ROW
# axis = 0 VERTICAL  , COLUMN BY COLUMN

# NOT EFFICIENT

data = []
for g in df.groupby( by = [ 'start_station_name']):
    data.append( len(g[1]) )


df['date'] = df['started_at'].dt.date
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by = ['date'])

data = []
for g in df.groupby(by = ['date']):
    data.append(len(g[1]))


plt.plot(data)
plt.show()
sys.exit(1)

print(df)

print(df.dtypes)
df['duration'] = df.apply( lambda row: (row['ended_at'] - row['started_at']).seconds / 60, axis = 1 )

data = df['rideable_type'].value_counts().to_dict()

df = df[ df['duration'] < 200 ]

el = df[ df['member_casual']  == 'member' ]
db = df[ df['member_casual']  == 'casual' ]

# plt.pie(data.values(), labels = data.keys())
#plt.hist( db['duration'], alpha=0.8, color='red' )
#plt.hist( el['duration'], alpha=0.8 )
plt.show()


