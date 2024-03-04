import sys
import pandas as pd
import numpy as np

df = pd.read_csv("w11.csv")

#* w11a.py:4: DtypeWarning: Columns (28) have mixed types. Specify dtype option on import or set low_memory=False.

#* Classification, Scoring: 10.000 rows is low
#* In scoring we may need even more (30-40 thousand)
#* There is a good number of features, nice!

#* 0: Settings
TARGET = 'price'

#* 1: Make the data usable

def transformDollar( value ):
    #: Delete, $ sign
    value = str(value).replace('$', '')
    #: Delete, , sign
    value = value.replace(',', '')
    #: Split by '.', get the first part
    value = value.split('.')[0]
    #: Transform into integer
    value = int(value)
    return value

#: Replace the '$' sign in the prices
df[TARGET] = df[TARGET].apply(transformDollar)

#: Transform into a "LOWER" information
# NOTE, Correlation only looks for "non-empty"

#: Remove the columns which have mostly NULL
del df['host_acceptance_rate']
del df['square_feet']
del df['monthly_discount']
del df['weekly_discount']

#* 2: Descriptive statistics
"""
from pandas_profiling import ProfileReport
prof = ProfileReport(df)
prof.to_file(output_file='w11_output.html')
"""

"""
for c in df:
    null_ratio = len(df[df[c].isnull()]) / len(df)
    if null_ratio > 0.0:
        print(round(null_ratio, 2), c)
"""

fill_empty = {}
for g in df.groupby(by = ['property_type']):
    fill_empty[ g[0] ] = {
        'bathrooms': g[1]['bathrooms'].mean(),
        'beds': g[1]['beds'].mean(), 
        'bedrooms': g[1]['bedrooms'].mean()
      }


def fillby( row, what: str ):
    
    # NOTE, Sometimes, pandas may have a small problem regarding to "nulls"
    if row[what] != None and not pd.isna(row[what]):
        return row[what]
    return fill_empty[ row['property_type'] ][ what ]

df['bathrooms'] = df.apply(lambda row: fillby(row, 'bathrooms'), axis = 1)
df['beds'] = df.apply(lambda row: fillby(row, 'beds'), axis = 1)
df['bedrooms'] = df.apply(lambda row: fillby(row, 'bedrooms'), axis = 1)

#* We tried, did not work
df['name'] = df['name'].str.lower()
df['wifi'] = df['name'].apply(lambda value: 'wifi' in value)


def findWords( df, columnname: str ) -> dict:
    output = {}

    total = 0
    for c in df[ columnname ].values:
        c = str(c).split(' ')
        for i in c:
            if i not in output:
                output[i] = 0
            output[i] += 1
            total += 1

    for c in output:
        output[c] = output[c] / total

    newoutput = {}
    for c in output:
        if output[c] > 0.005:
            newoutput[c] = output[c]

    return newoutput



df = df.sort_values(by = [TARGET])
ucuz = df[ 0:  int(len(df) / 2)]
bahali = df[ int(len(df) / 2): ]

"""
#* To find the differnet keywords used in "bahali" and "ucuz" houses
df_high = df[ df['price'] > df['price'].mean() ] #* The items which are greater than 214 [ expensive ]
df_low  = df[ df['price'] <= df['price'].mean() ] #* The items which are less than 214 [normal]

high = findWords( df_high, 'name' )
low = findWords( df_low, 'name' )


print(high.keys())
print(low.keys())
"""

bahali = ['family','pool','luxury']
ucuz = ['private', 'studio']

for c in bahali:
    df[c] = df['name'].apply(lambda value: c in value)

for c in ucuz:
    df[c] = df['name'].apply(lambda value: c in value)

df['lenname'] = df['name'].str.len()
df['wcname'] = df['name'].apply(lambda value: len(value.split(' ')))
del df['name']


# TODO host_about house_rules summary	space	description neighborhood_overview notes, transit, access, interaction,  -> these will be done, afternoon assignment

#* Because there is only ONE value for the experiences_offered, we delete it
del df['experiences_offered']


df['house_rules'] = df['house_rules'].isnull()
print(df['house_rules'].corr(df[TARGET]))

#* We do not need this, because we already have host_since
del df['host_id']

#* from what time, the customer is with us
df['host_since'] = pd.to_datetime( df['host_since'] ).dt.year

#* NOTE, you can convert it to, FIRST, SECOND, THRID AND OTHERS?
#! can also use df['host_location'] == df['host_location'].most()[0]
df['host_location'] = df['host_location'] == 'Sydney, New South Wales, Australia'
del df['host_location']

"""
IT DID NOT WORK OUT
df = pd.get_dummies(df, columns = ['host_response_time'])
for c in df:
    if 'host_response_time' in c:
        print(c, df[c].corr(df[TARGET]))
"""


del df['host_response_time']


def target_average(df, column: str, trgt):
    d = df.groupby(by = [column]).agg({trgt:'mean'}).to_dict()[trgt]
    df[column] = df[column].map(d)
    print(column, df[column].corr(df[trgt]))
    return df


df = target_average(df, 'host_response_rate', TARGET )
df = target_average(df, 'host_verifications', TARGET )

#! IT IS NOT IMPORTANT WHEN THE OWNER HAS ANSWERED
#! IT IS IMPORTANT THAT HE/SHE HAS ANSWERED

del df['zipcode']


df['room_type'] = df['room_type'] == 'Entire home/apt'

#: We delete bed_type, because, most of the values are SAME %99
del df['bed_type']




df['amenities'] = df['amenities'].apply(lambda value: str(value).replace("{", "").replace("}", "").split(','))
df['len_amenities'] = df['amenities'].apply(lambda value: len(value))

print(df['len_amenities'].corr(df[TARGET]))


"""


medium cardinality:
	host_neighbourhood
	street
	neighbourhood
	city
	smart_location
	

top 4 & others
	neighbourhood_cleansed
	property_type

"""