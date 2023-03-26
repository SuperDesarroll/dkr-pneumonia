from PIL import Image
from io import BytesIO
import numpy as np
import RX as rx

class ApiOOP():
            
    async def process_image(self,file):
        bytesImage = await file.read()        
        image= np.array(Image.open(BytesIO(bytesImage)))
        if file.filename.endswith("dcm"):
            dcm=rx.DCM()
            rxLoad = rx.RXRead(dcm)
            array,img2show= rxLoad.read_file_from_array(image)
            return array,img2show
        else:
            jpg=rx.JPGPNG()
            rxLoad = rx.RXRead(jpg)
            array,img2show= rxLoad.read_file_from_array(image)
            return array,img2show
