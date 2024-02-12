import sys
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Consutruct an algorithm
algorithm = RandomForestClassifier(max_depth=3, random_state=0)

df = pd.read_csv("w8_airlines_delay.csv") #! KOHNE, BILINEN, KNOWN DATA

# PREPROCESSING

del df['Flight'] # ID oldugu icin 
average_delays_per_airline = df.groupby(by = ['Airline']).agg({'Target': 'mean'}).to_dict()['Target'] 
df['Airline'] = df['Airline'].map(average_delays_per_airline)
df['Weekend'] = df['DayOfWeek'].isin( [6,7] )
df['Weekend'] = df['Weekend'].astype(int)
#! pd.get_dummies()

HH_C = df[ [ 'AirportFrom','AirportTo' ] ].value_counts(normalize=True).to_dict()

#* HH_A = haradan haraya average
HH_A = df.groupby(by = [ 'AirportFrom','AirportTo' ]).agg({'Target': 'mean'}).to_dict()['Target']

df['HH_C'] = df.apply( lambda row: HH_C[ (row['AirportFrom'], row['AirportTo']) ], axis = 1)
df['HH_A'] = df.apply( lambda row: HH_A[ (row['AirportFrom'], row['AirportTo']) ], axis = 1)

del df['AirportFrom']
del df['AirportTo']


df.to_csv("w8_latest.csv")


df = df.sample(frac = 0.10)

y = df['Target']
X = df.drop(columns = ['Target'])

algorithm.fit(X, y) # Train = Learn = Fit


import random

#* INCOMING, NEW DATA
index = random.randint( 0, len(X) - 1)
random_row = X.iloc[index]

# NOT A SINGLE ROW
# IT TAKES A LIST OF ROWS
results = algorithm.predict( [random_row] )
results = results[ 0 ]
print(index, random_row, "results", results)


x_results = algorithm.predict( X )
print("x_results", x_results)

X['TAHMIN'] = x_results
X['GERCEK'] = y

#* GERCEK	REAL	ACTUAL	TRUE
#* TAHMIN    PREDICTION 
#* SONUC	CORRECT	RESULT: [Real=Pred]
#* Accuracy is the average of Sonuc[Correct]

X.to_csv("w8_pred.csv")

#! ROW( x1,x2,x3 ... time, length, ..... ) ===> Target 1/0
#! [ROW( x1,x2,x3 ... time, length, ..... )] ===> [Target 1/0]




#* listenin icinde 1 row

#==================================================
#= IGNORE FOR NOW
estimator = algorithm.estimators_[5]
from sklearn.tree import export_graphviz
# Export as dot file
export_graphviz(estimator, out_file='tree.dot', 
                feature_names = X.columns,
                class_names =  ['NO', 'YES'],
                rounded = True, proportion = False, 
                precision = 2, filled = True)

# Convert to png using system command (requires Graphviz)
from subprocess import call
call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])
print(algorithm)
#==================================================




#= FIT == TRAIN == LEARN

sys.exit(1)

#! X = df[ ['Flight','Time','Length','Airline','AirportFrom','AirportTo','DayOfWeek'] ]




sonuc = algorithm.predict( YENI_GELEN_DATA ) # Tahminle, Karar ver, Execute


#! fit
#! predict



