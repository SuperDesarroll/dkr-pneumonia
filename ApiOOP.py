from PIL import Image
from io import BytesIO
import numpy as np
import IA as ia
import RX as rx

import base64
from io import BytesIO

class ApiOOP():
            
    async def process_image(self,file):
        bytesImage = await file.read()        
        image= np.array(Image.open(BytesIO(bytesImage)))
        if file.filename.endswith("dcm"):
            dcm=rx.DCM()
            rxLoad = rx.RXRead(dcm)
            self.array,self.img2show= rxLoad.read_file_from_array(image)
        else:
            jpg=rx.JPGPNG()
            rxLoad = rx.RXRead(jpg)            
            self.array,self.img2show= rxLoad.read_file_from_array(image)
        
        deepIA = ia.IA()
        self.label, self.proba, self.heatmap = deepIA.predict(self.array)            
        self.img2 = Image.fromarray(self.heatmap)
        self.img2 = self.img2.resize((250, 250), Image.ANTIALIAS)     
        
        buffered = BytesIO()
        self.img2.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue())

        return self.label, self.proba, img_str