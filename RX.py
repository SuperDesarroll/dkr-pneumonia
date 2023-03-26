from PIL import Image
import numpy as np
import pydicom as dicom
import cv2
from abc import ABC,abstractmethod

class RX(ABC):
    @abstractmethod

    def read_file_from_array(self,pixel_array):
        pass

class DCM(RX):
    
    def read_file_from_array(self,pixel_array):        
        img_array = pixel_array
        img2show = Image.fromarray(img_array)
        img2 = img_array.astype(float)
        img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
        img2 = np.uint8(img2)
        img_RGB = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)
        return img_RGB, img2show

class JPGPNG(RX):
       
    def read_file_from_array(self,pixel_array):        
        img_array = pixel_array
        img2show = Image.fromarray(img_array)
        img2 = img_array.astype(float)
        img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
        img2 = np.uint8(img2)
        img_RGB = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)
        return img_RGB, img2show

class RXRead():
    def __init__(self,c:RX):
        self.client = c            
    
    def read_file_from_array(self,pixel_array):        
        self.array, img2show = self.client.read_file_from_array(pixel_array)
        return self.array, img2show
    

            

