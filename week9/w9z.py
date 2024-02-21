import sys

f = "w9_car_price_prediction.csv"
target = "Price"

import pandas as pd 
df = pd.read_csv(f)

df['Mileage'] = df['Mileage'].apply(lambda value: int(str(value).replace(" km", "")))
df['Leather interior'] = df['Leather interior'].map({'Yes': 1, 'No': 0})
df['Wheel'] = df['Wheel'].map({'Left wheel': 1, 'Right-hand drive': 0})

df['Doors'] = df['Doors'].map({'04-May': 1, '02-Mar': 0, '>5': 0, None: 1})
df['Doors'] = df['Doors'].fillna(1)
df['Doors'] = df['Doors'].astype(int)


df = pd.get_dummies( df, columns = ['Category'])
df = pd.get_dummies( df, columns = ['Fuel type'])
df = pd.get_dummies( df, columns = ['Gear box type'])
df = pd.get_dummies( df, columns = ['Drive wheels'])


df = df[ df['Price'] < 100000 ]
df = df[ df['Price'] > 1000 ]

#! BUSINESS DEPARTMENT
#! I have completed the model
#! This model only works for cars whose price is in the range of [1000, 100000]

def fillLevy( row ):
    if row['Levy'] == '-':
        return row['Price'] * 0.107
    else:
        return int(row['Levy'])

df['Levy'] = df.apply( lambda row: fillLevy(row), axis = 1)


#avg = df.groupby(by = ['Model']).agg({target: 'mean'}).to_dict()[target]
#df['BASE'] = df['Model'].map(avg)
#print(df['BASE'].corr(df[target]))


#! BASE PRICE = if a model occoured more than 100 times, get the average price of "model"
#!              else get the average price of "manifacturer"










df = df.select_dtypes(exclude = ['object'])

# preprocessing
# normalization
# feature mining
# %95 SAME!!!
from sklearn.ensemble import RandomForestRegressor

clf = RandomForestRegressor(max_depth=5, random_state=0)

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

