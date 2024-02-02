import uvicorn
from fastapi import FastAPI
app = FastAPI()

@app.get("/hesapla")
def hesapla( yas, kredi_skoru ):
    yas = int(yas)
    kredi_skoru = int(kredi_skoru)
    if yas > 18 and yas < 25:
        if kredi_skoru > 500:
            return 5000
        else:
            return 2000
    elif yas > 24 and yas < 40:
        if kredi_skoru > 700:
            return 100000
        elif kredi_skoru > 500:
            return 50000
        else:
            return 25000
    else:
        return 2000


#: Run
if __name__ == '__main__':
	uvicorn.run(
		"w7m:app",
		host="0.0.0.0",
		port=6000,
		log_level="debug",
		reload=True,
	)

