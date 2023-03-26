# Estudiante: Dewins Murillo García
# Universidad Autónoma de Occidente
# Postgrado Inteligencia Artificial
# Entrega Preliminar:
# Proyectos de Inteligenciar Artificial 
# Aplicando Ingeniería de Software

# ApoOOP.py
# Clase inicial de la api
# Esta clase se encarga de preprocesar el archivo dependiendo de su extensión
# instanciando RX con sus distintos métodos abstractos.
# Al finalizar crea una imagen del mapa de calor y los transforma a base64

from PIL import Image
from io import BytesIO
import cv2
import numpy as np
import Classes.IA as ia
import Classes.RX as rx
import pydicom as dicom
import base64
from io import BytesIO

class ApiOOP():
    
    async def process_image(self,file):    
        file_location = f"files/{file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())   

        if file.filename.endswith("dcm"):      
            img = dicom.read_file(file_location)              
            img_array = img.pixel_array
            dcm=rx.DCM()
            rxLoad = rx.RXRead(dcm)
            self.array,self.img2show= rxLoad.read_file_from_array(img_array)
        else:
            img = cv2.imread(file_location)
            img_array = np.asarray(img)            
            jpg=rx.JPGPNG()
            rxLoad = rx.RXRead(jpg)            
            self.array,self.img2show= rxLoad.read_file_from_array(img_array)
        
        deepIA = ia.IA()
        self.label, self.proba, self.heatmap = deepIA.predict(self.array)            
        self.img2 = Image.fromarray(self.heatmap)
        self.img2 = self.img2.resize((250, 250), Image.ANTIALIAS)     
        
        buffered = BytesIO()
        self.img2.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue())

        return self.label, self.proba, img_str