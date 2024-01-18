
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




print(df['Continent'].value_counts(normalize=True).to_dict())

customer_visit_count = df['DocIDHash'].value_counts().to_dict()
print(list(customer_visit_count.items())[0:10])


EMPTY_PASSPORT_NUMBER = '0x5FA1E0098A31497057C5A6B9FE9D49FD6DD47CCE7C268E6548699E78E587AAEA'
customer_visit_count[EMPTY_PASSPORT_NUMBER] = 1

df['CustomerVisitCount'] = df['DocIDHash'].map(customer_visit_count)
#        VALUE                 KEY

"""
[
    ('0xF0F3DBC14E608DB89EB4A499B8DB16A8256AE765AEDFF8BC366FC64A019D1CBD', 15), 
    ('0xC397E9F80FD9A9AB7365734240F585038E9EBCCE93D875C631D0B56A35C5A59D', 12), 
    ('0xFAA092BD2DEC4643F642489240C07CAE8311FA20C376B3D3D6B62BCA5DA7F9E1', 10), 
    ('0xB73465DE229AC416DDED0A4DDFADB1428922CDDFFC84FF206EA7868784E04DEA', 10), 
    ('0x2D2771E932895A19D4BE999D2BD051F9E2B2ED0EF6F78D43892FEBFC460CA0D4', 10), ('0x7288D12D383C94B2D140A2045711DD48205EF14F389D755763E10FEEA2AB4211', 10), ('0x8DBF728E57E5FB92CB3700DF0984EC95DAD747A909A4C17719CFBB246AC4AE99', 8), ('0xF1073F20EE929DF91282F6FB3E1E13487BD56374B2A14600510234169CB23F10', 8), ('0x92640ECE7E2404E1412ED6DE32C5AF3C0C4F0CE74D9FF202A063B9123F2EDA7E', 7), ('0x912269DC9D88AC85354919F387AEF172B6F5DA0EE13FF5B224C651C2DB78E975', 7)]
"""

print(df['DocIDHash'].value_counts())


df = df.sort_values( 'NameHash' )

da = df[ df['DocIDHash'] == '0x5FA1E0098A31497057C5A6B9FE9D49FD6DD47CCE7C268E6548699E78E587AAEA' ][['NameHash', 'DocIDHash', 'Nationality']]
# SORT, ORDER
print(da)
da.to_csv("w5da.csv")



yaslar = {
    18: 'YOUNG',
    19: 'YOUNG',
    20: 'YOUNG',
    21: 'YOUNG',
    22: 'YOUNG',
    23: 'YOUNG',
    23: 'YOUNG',
    24: 'YOUNG',

    60: 'OLD',
    61: 'OLD',
    62: 'OLD',
    63: 'OLD',
}

def AgeType( age: int ) -> str:
    if age < 20: 
        return 'TEEN'
    if age < 30: 
        return 'VERY-YOUNG'
    if age < 40: 
        return 'YOUNG'
    if age < 60: 
        return 'MIDDLE AGE'
    return 'OLD'


def CustomerType(nationality:str) -> str:
    if nationality == 'PRT':
        return 'local'
    if nationality in ['AUT', 'BEL', 'BGR', 'HRV', 'CYP', 'CZE', 'DNK', 'EST', 'FIN', 'FRA', 'DEU', 'GRC', 'HUN', 'IRL', 'ITA', 'LVA', 'LTU', 'LUX', 'MLT', 'NLD', 'POL', 'PRT', 'ROU', 'SVK', 'SVN', 'ESP', 'SWE']: #Europe Union Countries
        return 'europe'
    return 'other'

# %90
europe_countries = [c for c, continent in continent_dictionary.items() if continent == 'Europe']



#! df['Age-YOUNG-OLD'] = df['Age'].map(yaslar)
#! df['Age-YOUNG-OLD'] = df['Age'] >= 60

df['Age-YOUNG-OLD'] = df['Age'].apply(AgeType)
df['CustomerType'] = df['Nationality'].apply(CustomerType)

print( df.query("Nationality=='AZE'")['Age'].count() )
print( df[ df['Nationality'] == 'AZE' ]['Age'].count() )


for g in df.groupby( by = ['Nationality'] ): # ==> SUB GROUPS
    #* name of the group = g[0]
    #* data of the group = g[1]
    print("==================")
    print(g[0])
    print(g[1]['Age'].mean())


#* ALL DATA == POPULATION [ALL PEOPLE IN AZERBAIJAN]
#* survey, poll ==> SUB PART, SMALL PART, SMALL PARTITION, SMALL GROUP ==> SAMPLE
# SHUFFLE
# RANDOMLY SELECT
print(df.sample(n = 1000))
print(df.sample(frac = 0.10))

