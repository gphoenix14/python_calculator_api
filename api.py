from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="API Calcolatrice", description="API REST per eseguire operazioni matematiche", version="1.0")

# Modello per la richiesta
class Operazione(BaseModel):
    numero1: float
    numero2: float

@app.get("/")
def home():
    return {"messaggio": "Benvenuto nell'API Calcolatrice. Usa /docs per la documentazione."}

@app.post("/addizione")
def addizione(op: Operazione):
    risultato = op.numero1 + op.numero2
    return {"operazione": "addizione", "risultato": risultato}

@app.post("/sottrazione")
def sottrazione(op: Operazione):
    risultato = op.numero1 - op.numero2
    return {"operazione": "sottrazione", "risultato": risultato}

@app.post("/moltiplicazione")
def moltiplicazione(op: Operazione):
    risultato = op.numero1 * op.numero2
    return {"operazione": "moltiplicazione", "risultato": risultato}

@app.post("/divisione")
def divisione(op: Operazione):
    if op.numero2 == 0:
        raise HTTPException(status_code=400, detail="Errore: divisione per zero non consentita.")
    risultato = op.numero1 / op.numero2
    return {"operazione": "divisione", "risultato": risultato}

if __name__ == "__main__":
    uvicorn.run("calculator_api:app", host="0.0.0.0", port=8000, reload=True)
