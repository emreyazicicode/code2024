
from w5additional import COUNTRY_CONTINENT
import pandas as pd

# NOTE: CustomerID, CustomerNo, CustomerNumber, Customer_ID, [some..]Code .......
#       usually this is "reference number", "FIN Number"
#       a) [Unique] [primary key, primary index] or [very close to unique]
#       b) Not null, not empty, not na, not .....
#       c) Categoric, no mathematical operations can be done, no comparison can be done

# df = pd.read_excel('w5.xlsx')
df = pd.read_csv('w5small.csv')

for c in df:
    # Number of unique items
    n = df[c].nunique()
    a = len(df)

    # Cardinality ==> number of unique items / all items
    # 1.0  == all unique [not always]
    # 0.85 == float [not always]
    print("CARDINALITY", c, n / a)


#* Nationality
print(df['Nationality'].value_counts().to_dict())  

#* To create a NEW column
comparison = df['Nationality'] == 'PRT'
# =  assign a value to a variable
# == compare that two of the sides are same or not
# a == b 
df['NativeTourist'] = comparison

# ['PRT', 'PRT', 'DEU', 'FRA' ...] == 'PRT'

# To create a new column, we must use another column [at least]
df['Older'] = df['Age'] > 70


d = {'x': 0, 'y': 1}
print(d['x'])
d['z'] = 2 # create a new value



# PRT
# PRT
# FRA
# ...

df['Continent'] = df['Nationality'].map( COUNTRY_CONTINENT )

#* give me the "VALUE" of given "DICTIONARY (COUNTRY_CONTINENT)" WHERE THE "KEY" IS IN Nationality

#* map ==> match, lookup

# Asia
# Europe
# America
# Africa




continent = pd.read_csv("w5continent.csv")
# TRANSFORMS TWO LISTS INTO A DICTIONARY, FIRST ONE IS KEYS, SECOND ONE IS VALUES
continent_dictionary = dict(zip(continent['Code'], continent['Continent']))
# df['Continent'] = df['Nationality'].map(continent_dictionary)


#print( continent_dictionary )
# TRANSFORMS A DICTIONARY TO TWO LISTS (one is keys, second is values)
my = {
    'a': 3,
    'b': 4,
    'c': 5
}

print( my.keys() )
print( my.values() )


# PIE CHART --> later
print(df['Nationality'].value_counts(normalize=True).to_dict())  

# Two lines below are exactly SAME
print("BEFORE", len(df))
#* df = df[ df['Age'] >= 18 ]
df = df.query('Age >= 18') 
print("AFTER", len(df))

# SELECT * FROM table WHERE age >= 18



print( df['Age'].describe() )
print( "max", df['Age'].max() )
print( "min", df['Age'].min() )
print( "mean", df['Age'].mean() )

print('-------------------------------------------------------------------')

print(df.describe())
print(df['Age'].describe())


print("Average Age", df['Age'].mean())
print( df.head(1000).mean().to_dict() )

print( df[ [] ] )

print("==================")
print(df[  ['AverageLeadTime','LodgingRevenue','OtherRevenue']  ].head(1000).mean().to_dict())


#* CONVERT THE TYPE OF A DATA - COLUMN
f = 3.7
i = int(f)
print(f, i)
print( df['LodgingRevenue'].astype( int ) )

print( df['LodgingRevenue'].round().astype( int ) )

print( df['LodgingRevenue'].round(1) ) # How many decimals

df['Age'] = df['Age'].fillna(df['Age'].mean())

df['Age'] = df['Age'].round(-1)

"""
i = 58.67
round(i, 1) => 58.7
round(i) = 59
round(i, -1) = 60

i = 52.67
round(i, 1) => 52.7
round(i) = 53
round(i, -1) = 50
"""


# The age of customership, age = 28 , TENURE = 3 (3 ildir bizimle calisiyor)





df['Age'] = df['Age'].astype(int)




df['Tenure'] = (df['DaysSinceCreation'] / 365).round(1)
"""
port rivoli baku
2022-may             creation, first enterance
2022-sep
2023-may
..

DaysSinceCreation  750 days have passed
"""

import uuid

print( uuid.uuid1() )

# ec552502-b50a-11ee-8e23-2154b3af2c0d

print(df.head(20))
df.to_csv("w5export.csv")



#dx = pd.read_html('https://www.babynamemeaningz.com/name/boy/Azerbaijani/alphabetically/A')
#print(dx)


print(df['NameHash'].value_counts())


print(df['Continent'].value_counts(normalize=True).to_dict())
