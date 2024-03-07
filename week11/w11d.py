from sklearn.metrics import roc_curve, auc, f1_score, recall_score, precision_score
import json
import numpy as np
import sys
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
#==============================================================================
df = pd.read_csv("w8_airlines_delay.csv") #! KOHNE, BILINEN, KNOWN DATA
df = df.sample(frac = 0.05) # Make it smaller
#==============================================================================
#= PREPROCESSING
del df['Flight'] # ID oldugu icin 
average_delays_per_airline = df.groupby(by = ['Airline']).agg({'Target': 'mean'}).to_dict()['Target'] 
df['Airline'] = df['Airline'].map(average_delays_per_airline)
df['Weekend'] = df['DayOfWeek'].isin( [6,7] )
df['Weekend'] = df['Weekend'].astype(int)
HH_C = df[ [ 'AirportFrom','AirportTo' ] ].value_counts(normalize=True).to_dict()
#* HH_A = haradan haraya average
HH_A = df.groupby(by = [ 'AirportFrom','AirportTo' ]).agg({'Target': 'mean'}).to_dict()['Target']
df['HH_C'] = df.apply( lambda row: HH_C[ (row['AirportFrom'], row['AirportTo']) ], axis = 1)
df['HH_A'] = df.apply( lambda row: HH_A[ (row['AirportFrom'], row['AirportTo']) ], axis = 1)
del df['AirportFrom']
del df['AirportTo']
for c in df:
    if df[c].nunique() > 2:
        df[c] = (df[c] - df[c].min()) - (df[c].max() - df[c].min())
#==============================================================================


"""
from sklearn.ensemble import IsolationForest
clf = IsolationForest(max_samples=100, contamination=0.01)
clf.fit(df)
y_pred_train = clf.predict(df)
y_pred_train = list(y_pred_train)

freq = {}
for i in set(y_pred_train):
    freq[ i ] = y_pred_train.count(i)

df['ANOMALY'] = y_pred_train

pd.set_option("display.precision", 3)

print( df[ df['ANOMALY'] == -1 ].describe() )
print( df[ df['ANOMALY'] == 1 ].describe() )
"""
# ==================================================================

#: Import operating system related library
import os
import pickle
from sklearn.cluster import KMeans

CLUSTER_COUNT = 5
max_val = 0
max_c = None

#: If those files are exist
if os.path.isfile("w11_kmeans.json") and os.path.isfile('w11_kmeans.pickle'):
    print('FILES ARE EXIST, SO WE LOAD FROM THEM')
    config = json.load(open('w11_kmeans.json'))
    print('CURRENT CONFIG', config)
    CLUSTER_COUNT = config['cluster_count']
    max_val = config['max_val']
    max_c = config['max_c']

    kmeans = pickle.load(open('w11_kmeans.pickle', 'rb'))
    labels = kmeans.predict( df.drop(columns = ['Target']) )
    df['CLUSTER'] = labels
else:
    print('FILES NOT EXISTS, WE TRAIN THE MODEL AND RE-CREATE FILES')
    
    kmeans = KMeans(n_clusters=CLUSTER_COUNT, random_state=0, n_init="auto")
    kmeans.fit(df.drop(columns = ['Target']))
    labels = kmeans.predict( df.drop(columns = ['Target']) )
    #* WB = write to file as "binary" (not textual)
    #: Save the kmeans model into a file, so that we can use it later
    pickle.dump( kmeans, open('w11_kmeans.pickle', 'wb') )
    
    #: We assign the cluster labels to each row
    df['CLUSTER'] = labels
    df = pd.get_dummies(df, columns = ['CLUSTER'])

    for c in df: # For each column in dataframe
        if 'CLUSTER' in c: # If the column has 'CLUSTER' word in it
            val = abs(df[c].corr(df['Target']))
            if val > max_val:
                max_val = val
                max_c = c

    print(max_c, max_val)

    json.dump({'max_c': max_c, 'max_val': max_val, 'cluster_count': CLUSTER_COUNT}, open('w11_kmeans.json', 'w'))
# ==================================================================


"""
#: Assign the found labels to dataset
 # 0, 1, 2, 3

for g in df.groupby(by = ['CLUSTER']):
    print(g[0], len(g[1]))
    cluster_centroid = g[1].mean().to_dict()
    cluster_centroid = {k:round(v, 3) for k,v in cluster_centroid.items()}
    #: We already know which cluster it belongs to
    del cluster_centroid['CLUSTER']
    print(cluster_centroid)

print(df)
"""





"""
# random
import random
def my_random() -> float:
    pass
random.randrange( 1, 100 )

def randrange( min, max ):
    return min + (max - min) * random.random()
"""

# ==================================================================
#* DIMENSION REDUCTION
from sklearn.decomposition import PCA
pca = PCA(n_components=1)
pca.fit( df.drop( columns = ['Target']) )
pca_component = pca.transform( df.drop( columns = ['Target']) )

df['PCA'] = pca_component
# ==================================================================
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
clf = LinearDiscriminantAnalysis()
clf.fit(df.drop(columns = ['Target']), df['Target'])
lda_component = clf.predict( df.drop(columns = ['Target']) )
df['LDA'] = lda_component
# ==================================================================

#* WHY DO WE MIX, SHUFFLE
df = df.sample( frac = 1.0 ) # 1.00 = %100  HEPSINI AL, SHUFFLE MIXTURE

#: Split into TRAIN AND TEST
limit = int(len(df) * 0.60) # FAIZ 60 ini train kumesi
train = df[ :limit ] #* start from begining to LIMIT
test  = df[ limit: ] #* start from LIMIT to END

#: Split into INPUT / OUTPUT
train_y = train['Target']
train_x = train.drop(columns = ['Target'])

test_y = test['Target']
test_x = test.drop(columns = ['Target'])

print("train_x.shape", train_x.shape)
print("test_x.shape", test_x.shape)
#==============================================================================

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

# NOTE: imbalanced dataset; 1 %90, 0 %10

#* Supervised learning, will it delay or not (FLIGHT)
clf0 = RandomForestClassifier(max_depth=8, random_state=0)
clf0.fit(train_x, train_y)
pred0 = clf0.predict( test_x )
print( 'Trained, RFC f1_score', f1_score( test_y, pred0 ) )

from sklearn.linear_model import LogisticRegression
clf2 = LogisticRegression()
clf2.fit(train_x, train_y)
pred2 = clf2.predict( test_x )
print( 'Trained, LR f1_score', f1_score( test_y, pred2 ) )

from sklearn.ensemble import AdaBoostClassifier
clf3 = AdaBoostClassifier(n_estimators=100, algorithm="SAMME",)
clf3.fit(train_x, train_y)
pred3 = clf3.predict( test_x )
print( 'Trained, AB f1_score', f1_score( test_y, pred3 ) )


ab = clf3.predict_proba( test_x )[:,1]
lr = clf2.predict_proba( test_x )[:,1]
rf = clf0.predict_proba( test_x )[:,1]

test_x[ 'AB' ] = ab
test_x[ 'LR' ] = lr
test_x[ 'RF' ] = rf

test_x[ 'Real' ] = test_y


test_x.to_csv("w11_test_voting.csv")

"""
from sklearn.svm import SVC
clf1 = SVC(gamma='auto')
clf1.fit(train_x, train_y)
pred1 = clf1.predict( test_x )
print( 'Trained, SVC f1_score', f1_score( test_y, pred1 ) )
"""


