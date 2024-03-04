import numpy as np
import sys
import uvicorn
import pandas as pd
from fastapi import FastAPI
import random
import pickle
import json
import os
#: Open the file
modelfile = open('airlinepickle.pickle', 'rb') #! Read binary
#: Load the model from the model file
clf = pickle.load(modelfile)
#: Close the file
modelfile.close()

app = FastAPI()



"""
PREPARE THIS DATA IN A DIFFERENT FILE
"""

#: Check file exists or not
if os.path.isfile("average_delays_per_airline.pickle"):
    average_delays_per_airline = pickle.load(open('average_delays_per_airline.pickle', 'rb'))
    HH_C = pickle.load(open('HH_C.pickle', 'rb'))
    HH_A = pickle.load(open('HH_A.pickle', 'rb'))
    print('loaded from pickle files')
else:
    #* Prepare the transform data [if not exists]
    df = pd.read_csv("w8_airlines_delay.csv")
    average_delays_per_airline = df.groupby(by = ['Airline']).agg({'Target': 'mean'}).to_dict()['Target']
    HH_C = df[ [ 'AirportFrom','AirportTo' ] ].value_counts(normalize=True).to_dict()
    HH_A = df.groupby(by = [ 'AirportFrom','AirportTo' ]).agg({'Target': 'mean'}).to_dict()['Target']
    #* Save to pickle files
    with open("average_delays_per_airline.pickle", "wb") as fp:
        pickle.dump(average_delays_per_airline, fp)  # encode dict into pickle
    with open("HH_C.pickle", "wb") as fp:
        pickle.dump(HH_C, fp)  # encode dict into pickle
    with open("HH_A.pickle", "wb") as fp:
        pickle.dump(HH_A, fp)  # encode dict into pickle




def processSingleRow(row):
    del row['Flight'] # ID oldugu icin 
    
    row['Airline'] = average_delays_per_airline[ row['Airline'] ]
    row['Weekend'] = row['DayOfWeek'] in [6,7]

    row['HH_C'] = HH_C[ ( row['AirportFrom'], row['AirportTo'] ) ]
    row['HH_A'] = HH_C[ ( row['AirportFrom'], row['AirportTo'] ) ]

    del row['AirportFrom']
    del row['AirportTo']
    
    return row

@app.get("/infer")
def infer( row ):

    print("1")
    row = json.loads( row )
    print("2")


    row = processSingleRow( row )
    print("3")

    #: We trick that we have a "dataframe" of a "single row"
    #: Then, we obtain a list of results, but the size of the results is "1", so 
    # row ==> single dictionary
    # [row] ==> a list of single rows [kinda like a dataframe]
    #: CLF.predict returns a list of outputs
    #* If we want to transform a "dictionary" (which a single row) into dataframe
    #* we put [] around it
    
    row = list(row.values())
    print("row", row)
    d = pd.DataFrame(data = [row])
    return clf.predict( d )

#data = {'Flight': '2313', 'Time':1296, 'Length': 141, 'Airline': 'DL', 'AirportFrom': 'ATL', 'AirportTo': 'HOU', 'DayOfWeek': 1}
#print(json.dumps(data))


# DATAFRAME = LIST OF ROWS


#: Run, if I am the main file
if __name__ == '__main__':
	uvicorn.run(
		"w10k:app",
		host="0.0.0.0",
		port=6000,
		log_level="debug",
		reload=True,
	)
