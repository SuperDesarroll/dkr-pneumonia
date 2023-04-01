# Estudiante: Dewins Murillo García
# Universidad Autónoma de Occidente
# Postgrado Inteligencia Artificial
# Entrega Preliminar:
# Proyectos de Inteligenciar Artificial 
# Aplicando Ingeniería de Software

# main.py
# Inicio del api
# Se debe consumir el método process_image
# cargando el archivo desde el swagger o enviando por parámetro 
# el objetoc archivo.
# Retorna:
# label = (Viral, Normal o Bacteria)
# proba = de 1 - 100 porcentaje de probabilidad de predicción
# heatmap = base64 imagen mapa de calor

from starlette.responses import RedirectResponse
from fastapi import FastAPI, UploadFile
from fastapi.encoders import jsonable_encoder
import src.apibag as apibag #importamos la clase inicial ApiBag

app = FastAPI() 

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs/")    

@app.post("/process_image/")
async def process_image(file: UploadFile):
    apiObj = apibag.ApiBag() #declaramos el objeto Api OOP
    label, proba, heatmap=await apiObj.process_image(file) #procesamos la imagen   
    return {"filename": file.filename,"label":label,"proba":proba,"heatmap":heatmap}