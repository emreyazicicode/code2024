import numpy as np
import sys
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt
#==============================================================================
df = pd.read_csv("w8_airlines_delay.csv") #! KOHNE, BILINEN, KNOWN DATA
df = df.sample(frac = 0.10)
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
#==============================================================================

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


#==============================================================================
# Consutruct an algorithm

algorithms = [
    RandomForestClassifier(max_depth=4, random_state=0),
    #KNeighborsClassifier(n_neighbors=3),
    #LinearSVC(dual="auto", random_state=0, tol=1e-5)
]

#! y = f( x1, x2, x3 )
for algorithm in algorithms:
    algorithm.fit(train_x, train_y) # Train = Learn = Fit
    #! WRONG algorithm.predict(train_x)
    tahmin_predicted_results = algorithm.predict( test_x )
    tahmin_probabilities = algorithm.predict_proba( test_x )


    print("PRED", tahmin_predicted_results)
    print("REAL", test_y.values)

    test_x['PRED'] = tahmin_predicted_results
    test_x['PROB'] = tahmin_probabilities[:,1]
    test_x['REAL'] = test_y
    test_x['CERT'] = np.abs(0.5 - test_x['PROB'])

    test_x['CORRECT'] = test_x['PRED'] == test_x['REAL']
    test_x['TP'] = test_x.apply(lambda row: row['PRED'] == 1 and row['CORRECT'] == True, axis = 1)
    test_x['TN'] = test_x.apply(lambda row: row['PRED'] == 0 and row['CORRECT'] == True, axis = 1)
    test_x['FP'] = test_x.apply(lambda row: row['PRED'] == 1 and row['CORRECT'] == False, axis = 1)
    test_x['FN'] = test_x.apply(lambda row: row['PRED'] == 0 and row['CORRECT'] == False, axis = 1)


    test_x['CORRECT'] = test_x['CORRECT'].astype(int)
    test_x['TP'] = test_x['TP'].astype(int)
    test_x['TN'] = test_x['TN'].astype(int)
    test_x['FP'] = test_x['FP'].astype(int)
    test_x['FN'] = test_x['FN'].astype(int)


    test_x = test_x.sort_values(by = ['PROB'], ascending=[False])

    test_x.to_csv("w8test.csv")


    print("ACCR", np.mean(test_y.values == tahmin_predicted_results))

#==============================================================================

"""
modelar = {}
for x in df['City'].unique():
    modelar[ x ] = df[ df['City'] == c ]['Level'].mode()[0]


istanbul === 4
baku == 3
london == 7


def fillfunction( row ):
    if row['Level'] != None:
        return row['Level']
    else:
        return modelar[ row['City'] ]

df['Level'] = df.apply( lambda row: fillfunction(row), axis = 1 )

"""


"""
xs = df[ df[ 'Target' ] == 0 ]['Time']
ys = df[ df[ 'Target' ] == 0 ]['Length']
plt.scatter(xs, ys, alpha = 0.2)

xs = df[ df[ 'Target' ] == 1 ]['Time']
ys = df[ df[ 'Target' ] == 1 ]['Length']
plt.scatter(xs, ys, alpha = 0.2)

plt.show()
"""