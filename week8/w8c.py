import numpy as np
import sys
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
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
# Consutruct an algorithm
algorithm = RandomForestClassifier(max_depth=3, random_state=0)
#==============================================================================
df = df.sample( frac = 1.0 ) #! IMPORTANT
limit = int(len(df) / 2)
train = df[ :limit ]
test  = df[ limit: ]
train_y = train['Target']
train_x = train.drop(columns = ['Target'])
test_y = test['Target']
test_x = test.drop(columns = ['Target'])


algorithm.fit(train_x, train_y) # Train = Learn = Fit
#! WRONG algorithm.predict(train_x)
predicted_results = algorithm.predict( test_x )

print("PRED", predicted_results)
print("REAL", test_y.values)

print("CRRT", np.mean(test_y.values == predicted_results))

