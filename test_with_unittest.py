# Estudiante: Dewins Murillo García
# Universidad Autónoma de Occidente
# Postgrado Inteligencia Artificial
# Entrega Preliminar:
# Proyectos de Inteligenciar Artificial 
# Aplicando Ingeniería de Software

# test_with_unittest.py
# Esta clase tiene distintas pruebas unitarias
# que se ejecutaran utilizando el comando siguiente:
# python -m unittest discover
# Las pruebas son:
# test_cargue_jpg: prueba que se cargue una imagen y se verifica las dimensiones
# para que cumpla con los requisitos del negocio
# test_predict: prueba la predicción de una imagen retornando una probabilidad
# de acuerdo con el negocio toda predicción debe cumplir con unos criterios mínimos
# de probabilidad en este caso debe ser superior al 50%

from unittest import TestCase
import Classes.RX as rx
import Classes.IA as ia

class TryTesting(TestCase):

    def test_cargue_jpg(self):        
        dcm=rx.JPGPNG()
        rxLoad = rx.RXRead(dcm)
        array, img2show = rxLoad.read_file("files/JPG/virus/person1501_virus_2611.jpeg")        
        assert (array.shape == (640, 1024, 3))

    def test_predict(self):
        dcm=rx.JPGPNG()
        rxLoad = rx.RXRead(dcm)
        array, img2show = rxLoad.read_file("files/JPG/virus/person1501_virus_2611.jpeg")        
        deepIA = ia.IA()
        label, proba, heatmap = deepIA.predict(array)        
        print(proba)
        assert (float(proba) >50)
