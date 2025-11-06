#!/usr/bin/env python
# coding: utf-8

# Si en lugar de usar el servicio Detect Faces de Rekognition, quisiéramos usar el de Detect Labels, procederíamos de la misma forma, cambiando únicamente el método a llamar y el procesamiento de la respuesta.

# In[1]:


import boto3


# <h4 style="color:orange;">Paso 1. Creamos el cliente de Rekognition</h4>

# In[2]:


AWS_ACCESS_KEY = 'ASIAQLLZGTZ5D5LNQSYC'
AWS_SECRET_KEY = 'lOi54j/VYGt4+nSdK0yw/C4iHdkiTRREuHsum+ET'
AWS_SESSION_TOKEN = 'IQoJb3JpZ2luX2VjEOT//////////wEaCXVzLXdlc3QtMiJHMEUCIQDCd64vv3F16DFbIyi5slYJBaSgtr9uHvzSzKiFZEy6AAIgOrdEky3dzGQ65kUrU4Amu/dsGHglT24SlMBE+JgVgtkqqQIIrf//////////ARAAGgwwMjQ0MTMzODAyMTgiDAV0lDEN0QxcJYnG8Sr9AT4p9K+BHEG2cRLn7Be2/FtW/yCLGT1tjKQ8QRIoQCOoXgCHEUNkee+i/gh1eKl9ZizZV5e+OSFpknCX1egBGTAgHQo3AgFUy0/fX/xWJ3Xtp/ryx3MSjPJNEUDh/ShUj3vDe29P+AosnRwKo6fsrQPCyCi1BGtHx5l2f+7RS2sTY/JK8SOaK/anx5U/lJrNwZgWeCIiqKejnwv9Qc+fXpIAyrqZkzaqSoUTeC4/S0yGMl5rVyr+7AFptyT8URmD2ca+8XNwmevDEVmWhmRiK4jMamV+PZXQwYxnSFHhfE4KtOI8FooXNTyeftQC+nUJGQdXeQA5KbjK9u6ZHAswofqzyAY6nQEDr9/0OaY7HpDv0CgSlPahPQjA3xoMa4KSzxp0tIdeDUYfzsSJ3KtjEnG5t9YSeMlFKB6gBhiy2RPB14QmWLtEJlC4LTINahhYbIvUnpcxTeRcoD04B2zeidEnrlmzI1XkebztxClHUcRn0wWcUCvgVKsdlFjeZ+YMdEtKo29pOekN+7JSuaiMTZGhjvnssdiCB/QSf6nU+dfrVvYu'
REGION = 'us-east-1'  # Cambia a la región donde tienes habilitado Rekognition

# Creamos el cliente de Rekognition con las credenciales
rekognition_client = boto3.client('rekognition', 
    region_name=REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    aws_session_token=AWS_SESSION_TOKEN)


# <h4 style="color:orange;">Paso 2. Leemos el fichero con el que queremos trabajar</h4>

# In[3]:


# Leemos la imagen desde el archivo en formato binario

IMAGE_FILE_PATH = "C:\\Users\\Administrador\\Documents\\carlos\\IABD--programacion-inteligencia-artificial\\Ejercicios\\Tarea-AWS\\imagenes\\cara1descarga.jpg"
with open(IMAGE_FILE_PATH, 'rb') as image_file:
    image_bytes = image_file.read()


# <h4 style="color:orange;">Paso 3. Realizamos la solicitud a DETECT_LABELS</h4>
# 

# In[4]:


# Realizar la solicitud DetectFaces al servicio de Rekognition. En este caso, cambian ligeramente los parámetros que recibe el método
response = rekognition_client.detect_labels(
    Image={'Bytes': image_bytes},
    MaxLabels=15,            # Mostrar hasta 15 etiquetas
    MinConfidence=95.0       # Solo etiquetas con confianza >= 90%    
)


# <h4 style="color:orange;">Paso 4. Procesamos la respuesta</h4>
# 

# In[5]:


print(response)


# **Estructura de la respuesta**
# 
# La respuesta de detect_labels es un diccionario que contiene información sobre las etiquetas detectadas. Donde: 
# * **Labels**: Contiene las etiquetas detectadas con:
#     1. **Name**: El nombre de la etiqueta (por ejemplo, "Person", "Tree").
#     2. **Confidence**: La confianza de que la etiqueta sea correcta, en porcentaje.
#     3. **Instances**: Si aplica, contiene instancias de los objetos detectados con su BoundingBox (rectángulo de localización).
#     4. **Parents**: Las categorías generales a las que pertenece la etiqueta (por ejemplo, "Person" puede tener "Human" como padre).
# 
# 

# In[6]:


# Mostrar etiquetas detectadas
for label in response['Labels']:
    print(f"Etiqueta: {label['Name']}, Confianza: {label['Confidence']}, Categorías superiores:{label['Parents']}")


# In[ ]:




