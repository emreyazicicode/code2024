
import pandas as pd

"""
#* MERGING MORE THAN ONE FILE WITH SAME STRUCTURE!!
from os import listdir
from os.path import isfile, join

mypath = 'week6dataset/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#* LIST OF FILE NAMES


alldata = []
for f in onlyfiles:
    df = pd.read_csv(mypath + f)
    alldata.append( df )

singledataframe = pd.concat( alldata )
print(singledataframe)

singledataframe.to_csv("w6-b.csv", index=None)

"""

df = pd.read_csv("w6-b.csv")
#del df['image']
#del df['link']
#del df['name']
#df.to_csv("w6-b.csv", index=None)
df = df.sample(n = 100000)
del df['Unnamed: 0']

#* discount_price
#* actual_price
#* ₹7,989


def convert( value: str ) -> float:
    value = str(value)
    value = value.replace('₹', '')
    value = value.replace(',', '')
    return float(value) * 0.02

df['discount_price'] = df['discount_price'].apply(convert)
df['actual_price'] = df['actual_price'].apply(convert)
df['discount_ratio'] = df['discount_price'] / df['actual_price'] # FAIZ KAC INDIRIM YAPMIS
df = df.dropna()
import matplotlib.pyplot as plt

#print(df.dtypes)
#! ~ ==> NOT
#! isin( ['x', 'y', 'z'] ) ONE OF THEM
#! ~ isin( ['x', 'y', 'z'] ) NOT ONE OF THEM

#! df = df[ ~ df['no_of_ratings'].isin(['FREE Delivery by Amazon', 'Only 1 left in stock.', 'Only 2 left in stock.', 'Usually dispatched in 3 to 4 weeks.']) ]

df = df[ ~ df['no_of_ratings'].str.contains('[A-Za-z]') ]
df['no_of_ratings'] = df['no_of_ratings'].apply(lambda value: float(str(value).replace(',', '')))
nof_ratings = sorted(list(df['no_of_ratings'].unique()))

df['ratings'] = df['ratings'].astype(float)

print(df.dtypes)

#plt.scatter( df['actual_price'], df['ratings'] )
#plt.show()



#* df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
#* df['Churn'] = df['Churn'].replace('Yes', 1).replace('No', 0)


"""
import numpy as np

a = [20, 20, 21, 19, 18, 19, 19, 19, 20, 22, 21, 20, 20, 20, 20, 20, 21, 20, 20]
print(np.mean(a), np.std(a))
b = [10, 1, 40, 50, 2, 11, 25, 40, 4, 3, 7, 18, 26, 39, 40, 26, 32, 11, 12, 7, 9]
print(np.mean(b), np.std(b))


plt.hist( a )
plt.hist( b )
plt.show()

"""

#* get only the numerical variable names
numerics = list( df.select_dtypes(exclude=['object']).columns )
print(numerics)

print(df.shape)

cols = []
for n in numerics:
    avg = df[n].mean()
    std = df[n].std()
    df[f'is_{n}_upper_outlier'] = df[n] > avg + 3 * std
    cols.append(f'is_{n}_upper_outlier')

print("cols", cols)

def numberof_outlier( row ):
    total = 0
    for c in cols:
        total += row[c]
    return total

#* DIFFERENT TYPE OF USAGE OF APPLY
#* IF WE USE APPLY FOR "DATAFRAME" NOT A COLUMN
df['NUMBER_OF_OUTLIERS'] = df.apply(lambda row: numberof_outlier(row), axis = 1)
df['NUMBER_OF_OUTLIERS_2'] = df[ cols ].sum(axis = 1)


"""
#! CODE BELOW DIRECTLY FILTERS DATA
for n in numerics:
    avg = df[n].mean()
    std = df[n].std()
    df = df[ df[n] < avg + 3 * std ]
    df = df[ df[n] > avg - 3 * std ]

"""

print(df.shape)
df = df[ df['NUMBER_OF_OUTLIERS'] < 2 ]
print(df.shape)
df.to_csv("w6_out.csv")
