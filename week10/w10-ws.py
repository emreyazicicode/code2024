
#! SKELETON

#==============================================================================
#= TRAIN FILE 

#* Load dataset
df = pd......

#* Process the data, norm, transform, fill empties...
df['xxx'] = df.apply....

#* Model Create
clf = RandomForest()
clf.fit(x, y)

#* Dump to file, pickle
pickle.dumps( clf, 'mymodel.pickle' )

#==============================================================================

#==============================================================================
#= WEB SERVICE

#* Load dataset
clf = pickle.load( 'mymodel.pickle' )

#* Create a FastAPI application
app = FastAPI()

#* Web service infer function
app.post( '/infer' )
def infer( row: str ):

    #* 1: Transform into [json]
    row = json.loads( row )
    
    #* 2: Make transformations
    row['xxx'] = HH_C[ row['xxy'] ]

    #* 3: Apply model
    return clf.predict( [row] )[ 0 ]

#* Run, if I am the main file
if __name__ == '__main__':
	uvicorn.run(
		"w10k:app",
		host="0.0.0.0",
		port=6000,
		log_level="debug",
		reload=True,
	)
#==============================================================================

#==============================================================================
#= CRONJOB, SCHEDULED JOB

#* Load dataset
clf = pickle.load( 'mymodel.pickle' )

#* Load the NEW dataset
df = pd.read_csv( "NEW DATASET")

#* Process the data, norm, transform, fill empties...
df['xxx'] = df.apply....

#* PREDICT(!)
results = clf.predict( df )

#* Write the results to somewhere
results.to_csv("x.csv")

#==============================================================================


@app.post('/sdfsfsfsdd')
def x(asdfdfs):
    pass



#* calling the function
x(34)
#! I want the function (x) to be called from OUTSIDE
