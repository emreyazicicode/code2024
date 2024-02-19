
#! GOAL = "MAKE USE OF DATA"
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

f = "carins.csv"
target = "is_claim"
df = pd.read_csv(f)


#! CLEANING
#! DATA FILL
#! TRANSFORMATION
#* Flag
F = ['is_adjustable_steering','is_tpms','is_parking_sensors','is_parking_camera',
     'is_front_fog_lights', 'is_rear_window_wiper', 'is_rear_window_washer',
       'is_rear_window_defogger', 'is_brake_assist', 'is_power_door_locks',
       'is_central_locking', 'is_power_steering',
       'is_driver_seat_height_adjustable', 'is_day_night_rear_view_mirror',
       'is_ecw', 'is_speed_alert', 'is_esc']
for f in F:
    df[f] = df[f].map({'Yes': 1, 'No':0})

#* Flag, NOTE, if there are only "two" values, make it like a flag / binary
df['transmission_type'] = df['transmission_type'].map({'Automatic': 1, 'Manual': 0})
df['steering_type'] = df['steering_type'].map({'Power': 1, 'Electric': 0, 'Manual': 1})
df['rear_brakes_type'] = df['rear_brakes_type'].map({'Drum': 1, 'Disc': 0})

#* Narrow - downcast
df['upsegment'] = df['segment'].apply(lambda value: value[0])
#* Value Mapping
M = {
    #* We have transformed a categorical variable into an ordinal variable
    'segment': {'A': 1, 'B1': 2, 'B2': 3, 'C1': 4, 'C2': 5, 'Utility': 6},
    'engine_type': {'1.5 Turbocharged Revotron':1,'1.0 SCe':2,'K10C':2,'G12B':2,'F8D Petrol Engine':2,'i-DTEC':2,'1.5 L U2 CRDi':2,'K Series Dual jet':3,'1.2 L K Series Engine':3,'1.5 Turbocharged Revotorq':3,'1.2 L K12N Dualjet':3}
}
for m in M:
    df[m] = df[m].map( M[m] )

TA = ['area_cluster', 'model']
#* Apply the target average
for ta in TA:
    d = df.groupby(by=[ta]).agg({target:'mean'}).to_dict()[target]
    df[ta] = df[ta].map(d)
D = ['make', 'fuel_type', 'upsegment']
for d in D:
    df = pd.get_dummies( df, columns=[d] )

#* Parse
df['max_torque'] = df['max_torque'].apply(lambda value: value.split('Nm')[0])
df['max_torque'] = df['max_torque'].astype(float)

df['max_power'] = df['max_power'].apply(lambda value: value.split('bhp')[0])
df['max_power'] = df['max_power'].astype(float)

#! NORMALIZATION
N = ['population_density']
for n in N:
    df[n] = (df[n] - df[n].min()) / (df[n].max() - df[n].min())

#! FEATURE MINING
df['is_new'] = df['age_of_car'] == 0.0
df['is_new'] = df['is_new'].astype(int)
df['p1'] = df['policy_tenure'] > 1.0
df['p2'] = df['policy_tenure'] < 0.1

df['p1'] = df['p1'].astype(int)
df['p2'] = df['p2'].astype(int)

#! FEATURE MERGING
df['fm1'] = (df['make_2'] == 0) & (df['is_new'] == 1)
df['fm2'] = (df['make_4'] == 0) & (df['is_new'] == 1)
df['fm1'] = df['fm1'].astype(int)
df['fm2'] = df['fm2'].astype(int)





"""
AFTERNOON EXERCISE
def enrichment( df, col, type ):
    if type == 'log':
        df[ col + '_log' ] = np.log(df[col])
    if type == 'sqrt':
        df[ col + '_sqrt' ] = np.sqrt(df[col])

    return df

df = enrichment(df, 'gross_weight', 'log')
"""

#* HOW TO USE A CATEGORIC VARIABLE
#* 1 dummy
#* 2 dummy but some (London, New york 500 tane cities, top 10, OTHERS)
#* 3 target average
#* 4 usage ratio
#* 5 grouping


#* numeric olmayanlari silelim
print(df.shape)
df = df.select_dtypes(exclude = ['object'])
print(df.shape)

#* MLP HARD NORMALIZE
for c in df:
    r = (df[c].max() - df[c].min())
    df[c] = (df[c] - df[c].min()) / r



#= TRAIN TEST SPLITTING
#! TRAIN TEST etc

df = df.sample(frac = 1.0)


"""
print(df[target].value_counts())
plt.hist( df[ df[target] == 0].sample(n = 3748)['policy_tenure'], alpha = 0.5 )
plt.hist( df[ df[target] == 1]['policy_tenure'], alpha = 0.5 )
plt.show()
sys.exit(1)
"""

limit = 0.60
limit = int(len(df) * limit)

train = df[:limit]
test = df[limit:]
print("train.shape", train.shape)

ones = train[ train[target] == 1]
zeros = train[ train[target] == 0]

small_zeros = zeros.sample(n = len(ones)) #! EQUAL

train = pd.concat( [ones, small_zeros] )
train = train.sample(frac = 1.0) # Shuffle
print("train.shape", train.shape)

#* Split vertical, inputs, output
train_X = train.drop( columns = [target])
train_y = train[target]

test_X = test.drop( columns = [target])
test_y = test[target]

#= MODELLING

clf = RandomForestClassifier(max_depth=7, random_state=0)
#clf = XGBClassifier(n_estimators=50, max_depth=6, learning_rate=1, objective='binary:logistic')
#clf = MLPClassifier(random_state=1, max_iter=300)
#clf = KNeighborsClassifier(n_neighbors=3)

clf.fit(train_X, train_y)

tahmin = clf.predict(test_X)


"""
test_X['tahmin'] = tahmin
test_X['real'] = test_y
test_X.to_csv("preprocessed.csv")
"""

print("accuracy", clf.score(test_X, test_y))
print("f1_score", f1_score(test_y, tahmin))
print(tahmin, np.mean(tahmin))


cross_table = pd.crosstab(test_y, tahmin, rownames=['Actual'], 
colnames=['Predicted'], dropna=False)

print(cross_table)


