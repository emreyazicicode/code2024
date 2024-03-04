
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/infer")
def infer( row ):
    print("DISARIDAN GELEN", row)
    # .......
    

#: Run, if I am the main file
if __name__ == '__main__':
	uvicorn.run(
		"w10-ildirim:app",
		host="0.0.0.0",
		port=6000,
		log_level="debug",
		reload=True,
	)
