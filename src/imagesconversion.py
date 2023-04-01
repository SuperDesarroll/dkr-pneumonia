# Estudiante: Dewins Murillo García
# Universidad Autónoma de Occidente
# Postgrado Inteligencia Artificial
# Entrega Preliminar:
# Proyectos de Inteligenciar Artificial 
# Aplicando Ingeniería de Software

# RX.py (abstract)
# Esta clase tiene como objetivo procesar la imagen de acuerdo al tipo 
# de imagen, pueden ser jpeg o dicom, además puede tratar la imagen
# a partir de un array

from PIL import Image
import numpy as np
import pydicom as dicom
import cv2
from abc import ABC,abstractmethod

class RX(ABC):
    @abstractmethod
    def read_file(self,path):
        pass

    @abstractmethod
    def read_file_from_array(self,pixel_array):
        pass

class DCM(RX):
    
    def read_file(self,path):
        img = dicom.read_file(path)
        img_array = img.pixel_array
        img2show = Image.fromarray(img_array)
        img2 = img_array.astype(float)
        img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
        img2 = np.uint8(img2)
        img_RGB = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)
        return img_RGB, img2show

    def read_file_from_array(self,pixel_array):        
        img_array = pixel_array
        img2show = Image.fromarray(img_array)
        img2 = img_array.astype(float)
        img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
        img2 = np.uint8(img2)
        img_RGB = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)
        return img_RGB, img2show

class JPGPNG(RX):
    
    def read_file(self,path):
        img = cv2.imread(path)
        img_array = np.asarray(img)
        img2show = Image.fromarray(img_array)
        img2 = img_array.astype(float)
        img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
        img2 = np.uint8(img2)
        return img2, img2show

    def read_file_from_array(self,pixel_array):        
        img_array = pixel_array
        img2show = Image.fromarray(img_array)
        img2 = img_array.astype(float)
        img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
        img2 = np.uint8(img2)        
        return img2, img2show

class RXRead():
    def __init__(self,c:RX):
        self.client = c            
    
    def read_file(self,path):        
        self.array, img2show = self.client.read_file(path)
        return self.array, img2show
    
    def read_file_from_array(self,pixel_array):        
        self.array, img2show = self.client.read_file_from_array(pixel_array)
        return self.array, img2show
    

            

