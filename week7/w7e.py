
#: Imports
import sys
import pandas as pd
#: 
df = pd.read_csv("w6_202010-divvy-tripdata_small.csv")

df['rideable_type_isnull'] = df['rideable_type'].isnull()

print( df[ ['rideable_type', 'rideable_type_isnull'] ] )

df = pd.read_csv("w5_application_data_small.csv")

for c in df.select_dtypes(include=['object']):
    da = pd.get_dummies( df, columns=[c] )
    for q in da:
        if c in q:
            corr = da[q].corr(da['TARGET'])
            if abs(corr) > 0.05:
                print(q, corr)


import matplotlib.pyplot as plt

#plt.scatter( df['AMT_INCOME_TOTAL'], df['AMT_ANNUITY'] )
#plt.show()
#sys.exit(1)
df1 = df[df['TARGET'] == 1] 

df0 = df[df['TARGET'] == 0].sample(n = len(df1))

print(len(df0), len(df1))

df = pd.concat([df0, df1])

df['DAYS_BIRTH'] = df['DAYS_BIRTH'] / 365
df['DAYS_BIRTH'] = df['DAYS_BIRTH'].apply(lambda value : -1 * value )

t = 'DAYS_BIRTH'
# df = df[ df[t] < df[t].max() * 0.33 ]
plt.hist(df[ df['TARGET'] == 0][t], alpha= 0.5)
plt.hist(df[ df['TARGET'] == 1][t], alpha = 0.5)

print(df[ df['TARGET'] == 0][t].mean())
print(df[ df['TARGET'] == 1][t].mean())

"""
for v in df['ORGANIZATION_TYPE'].unique():
    plt.hist( df[df['ORGANIZATION_TYPE'] == v]['AMT_INCOME_TOTAL'], alpha=0.5 )
"""

plt.show()