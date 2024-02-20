#: Imports
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier
import matplotlib.pyplot as plt
import sys
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import f1_score
import seaborn as sns

#* Load the dataset
f = "w9_Loan_Default.csv"
target = "Status"
df = pd.read_csv(f)

#* Delete unnecessary columns
del df['year']

#* Transform the binary variables to flag
df['approv_in_adv'] = df['approv_in_adv'].map({'nopre': 0, 'pre': 1})
df['open_credit'] = df['open_credit'].map({'nopc': 0, 'opc': 1})
df['business_or_commercial'] = df['business_or_commercial'].map({'nob/c': 0, 'b/c': 1})

#! .........
"""
#! Note that, we have seen which ones are empty/null when the target is "1"
df = df[ df[target] == 1 ]
print(df.info())
sys.exit(1)
"""

df = df.drop(columns = ['rate_of_interest','Interest_rate_spread','Upfront_charges'])
df = df.dropna()
df = df.select_dtypes(exclude = ['object'])


#* Resample data, shuffle
df = df.sample(frac = 1.0)


#* Split into train test dataset
limit = 0.60
limit = int(len(df) * limit)

train = df[:limit]
test = df[limit:]


#* Rebalance the dataset
ones = train[ train[target] == 1]
zeros = train[ train[target] == 0]

print("ONES/ZEROS", len(ones), len(zeros))

small_zeros = zeros.sample(n = len(ones)) #! EQUAL

train = pd.concat( [ones, small_zeros] )

print("X1", train.shape)

train = train.sample(frac = 1.0) # Shuffle

#* Split vertical, inputs, output
train_X = train.drop( columns = [target])
train_y = train[target]

test_X = test.drop( columns = [target])
test_y = test[target]


clf = RandomForestClassifier(max_depth=7, random_state=0)
#clf = XGBClassifier(n_estimators=50, max_depth=6, learning_rate=1, objective='binary:logistic')
#clf = MLPClassifier(random_state=1, max_iter=300)
#clf = KNeighborsClassifier(n_neighbors=3)

#* Train
clf.fit(train_X, train_y)

tahmin = clf.predict(test_X)
prob = clf.predict_proba( test_X )
prob = prob[:,1] #* predict_proba returns the probability of "0 zeros" and "1 ones", we only take ones

print("f1_score", f1_score(test_y, tahmin))


test_X['tahmin'] = tahmin
test_X['real'] = test_y
test_X['prob'] = prob

test_X.sample(n = 5000).to_csv("w9-output.csv")

