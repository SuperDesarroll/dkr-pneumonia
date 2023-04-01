# dkr_pneumonia
Docker python tensorflow pneumonía

# Estudiante: Dewins Murillo García
Universidad Autónoma de Occidente
Postgrado Inteligencia Artificial
Entrega Final:
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


1. La aplicación inicia con el archivo main.py que su vez instancia el un objeto de la clase ApiOOP.py

> El archivo WilhemNet_86.h5 se encuentra en el zip que nos enviaron junto con el enlace del repositorio.

2. Las pruebas unitarias inician con el siguiente comando ubicado en la raiz del proyecto: 

>`pytest`

Implementaciones

1. Pueden cargar archivos con extensión dcm y jpeg

> Las imagenes RX se encuentran en la carpeta sample-images

2. Se Aplica Cohesión y acoplamiento en todos los métodos

> Los métodos creados son específicos para sus funciones

3. Se aplica Abstract en las clases RX y Export

> En este patrón de diseño creamos funciones de cargue y exportar respectivos

4. Se implmenta Patrón Strategy para que actué de acuerdo al comportamiento del tipo de archivo y los documentos a exportar

3. Se Implementa Pruebas unitarias de las clases IA y RX

> La carpeta tests contiene las 2 pruebas unitarias

ALGUNAS VISTAS:

**Swagger Metodo POST Procesar Imagen:**
![Respuesta](https://raw.githubusercontent.com/SuperDesarroll/dkr_pneumonia/main/screens/Api03.jpeg "Respuesta")

**Respuesta Label, Probabilidad y HeatMap**
![Respuestas](https://raw.githubusercontent.com/SuperDesarroll/dkr_pneumonia/main/screens/Api02.jpeg "Respuestas")

**HeatMap**
![Heatmap](https://raw.githubusercontent.com/SuperDesarroll/dkr_pneumonia/main/screens/Api01.jpeg "Heatmap")

El heatmap se puede visualizar online en este https://codebeautify.org/base64-to-image-converter

Pruebas Unitarias

**Comando pytest**

![comandopytest](https://raw.githubusercontent.com/SuperDesarroll/dkr_pneumonia/main/screens/App04.jpeg "Comando pytest")

**Comando pytest resultado**

![comandopytestresultado](https://raw.githubusercontent.com/SuperDesarroll/dkr_pneumonia/main/screens/App05.jpeg "Comando pytest resultado")
