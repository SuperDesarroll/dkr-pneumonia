# dkr_pneumonia
Docker python tensorflow pneumonía

# Estudiante: Dewins Murillo García
Universidad Autónoma de Occidente
Postgrado Inteligencia Artificial
Entrega Preliminar:
Proyectos de Inteligencia Artificial 
Aplicando Ingeniería de Software

# main.py
Inicio del la api
Se debe consumir el método process_image
cargando el archivo desde el swagger o enviando por parámetro 
el objetoc archivo.

Retorna:
- label = (Viral, Normal o Bacteria)
- proba = de 1 - 100 porcentaje de probabilidad de predicción
- heatmap = base64 imagen mapa de calor


1. La aplicación inicia con el archivo ApiOOP.py

> El archivo WilhemNet_86.h5 se encuentra en el zip que nos enviaron junto con el enlace del repositorio.

2. Las pruebas unitarias inician con el comando: 

>`python -m unittest discover`

Implementaciones

1. Pueden cargar archivos con extensión dcm y jpeg

> Las imagenes RX se encuentran en la carpeta sample-images

2. Se Aplica Cohesión y acoplamiento en todos los métodos

> Los métodos creados son específicos para sus funciones

3. Se aplica Abstract en las clases RX y Export

> En este patrón de diseño creamos funciones de cargue y exportar respectivos

4. Se implmenta Patrón Strategy para que actué de acuerdo al comportamiento del tipo de archivo y los documentos a exportar

3. Se Implementa Pruebas unitarias de las clases IA y RX

> El archivo test_with_unittest.py contiene las 2 pruebas unitarias

ALGUNAS VISTAS:

**Swagger Metodo POST Procesar Imagen:**
![Respuesta](https://raw.githubusercontent.com/SuperDesarroll/dkr_pneumonia/main/Pantallas/Api03.jpeg?token=GHSAT0AAAAAAB5QOPAIICW2D7SOWMRILYESZBAXONQ "Respuesta")

**Respuesta Label, Probabilidad y HeatMap**
![Respuestas](https://raw.githubusercontent.com/SuperDesarroll/dkr_pneumonia/main/Pantallas/Api02.jpeg?token=GHSAT0AAAAAAB5QOPAIQNHJVLWWR5OGKOB6ZBAXPXA "Respuestas")

**HeatMap**
![Heatmap](https://raw.githubusercontent.com/SuperDesarroll/dkr_pneumonia/main/Pantallas/Api01.jpeg?token=GHSAT0AAAAAAB5QOPAJEE73AEZLK773M5CGZBAXNNQ "Heatmap")

El heatmap se puede visualizar online en este https://codebeautify.org/base64-to-image-converter
