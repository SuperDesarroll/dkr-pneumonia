from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs/")    

@app.get("/validar/{numero}")
def validarcapicua(numero:str):
    respuesta = "No es capicua"
    print("validando")

    if numero==numero[::-1]:
        respuesta = "Es capicua"
    return {
        "numero":numero,
        "validacion":respuesta
    }