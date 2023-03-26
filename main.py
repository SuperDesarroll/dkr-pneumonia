from starlette.responses import RedirectResponse
from fastapi import FastAPI, UploadFile
import ApiOOP as apiOOP

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

@app.post("/process_image/")
async def process_image(file: UploadFile):
    apiObj = apiOOP.ApiOOP()    
    array, img2show =await apiObj.process_image(file)
    return {"filename": file.filename}