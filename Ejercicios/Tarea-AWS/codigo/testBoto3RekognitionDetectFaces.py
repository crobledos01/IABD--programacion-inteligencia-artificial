#!/usr/bin/env python
# coding: utf-8

# Si preferimos usar la **API de Python de Amazon Rekognition** en lugar de realizar llamadas HTTP directas, a través de la API REST HTTP, necesitamos descargar la librería **boto3**, que es el SDK de AWS para Python. Esto simplifica bastante la interacción con los servicios de AWS, ya que boto3 maneja automáticamente las firmas, autenticación y creación de las solicitudes.
# 
# 

# Lo primero que tenemos que hacer es instalar **boto3** si no lo tenemos ya instalado:
# 

# In[1]:



# In[2]:


import boto3


# <h4 style="color:orange;">Paso 1. Creamos el cliente de Rekognition</h4>

# Existen diferentes formas de especificar las credenciales con las que vamos hacer las llamadas:
# 
# 1. Usar el archivo de configuración **~/.aws/credentials**
#     El archivo debe residir en:
#         Linux/macOS: ~/.aws/credentials
#         Windows: C:\Users\TU_USUARIO\.aws\credential
#         
#     El archivo sigue el formato de secciones de perfiles, donde cada perfil está representado por un bloque entre corchetes   ([profile-name]). El perfil por defecto debe ser nombrado como [default]. Cada perfil puede tener las siguientes claves:
#         aws_access_key_id: Tu clave de acceso (access key).
#         aws_secret_access_key: Tu clave secreta (secret key).
#         aws_session_token (opcional): Token de sesión para credenciales temporales (si aplica).    
#  
#     
#     Por ejemplo:
#     
#      [default]
#      aws_access_key_id = YOUR_ACCESS_KEY_ID
#      aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
#      aws_session_token = YOUR_PROD_SESSION_TOKEN  # Solo si usas credenciales temporales
#      [dev]
#      aws_access_key_id = YOUR_DEV_ACCESS_KEY_ID
#      aws_secret_access_key = YOUR_DEV_SECRET_ACCESS_KEY
#      aws_session_token = YOUR_PROD_SESSION_TOKEN  # Solo si usas credenciales temporales    
# 
#   
# 
# 2. **Usar variables de entorno**:
# 
#     En el bash de linux:
#         export AWS_ACCESS_KEY_ID=your_access_key_id
#         export AWS_SECRET_ACCESS_KEY=your_secret_access_key
#         export AWS_SESSION_TOKEN=your_session_token   # Solo si tienes credenciales temporales
#         
#     En el terminal cmd o powershell de Windows:
#         set AWS_ACCESS_KEY_ID=your_access_key_id
#         set AWS_SECRET_ACCESS_KEY=your_secret_access_key
#         set AWS_SESSION_TOKEN=your_session_token   # Solo si tienes credenciales temporales
# 
# 
# 3. **Usar variables en nuestro código python con los valores**.
# 

# In[3]:




# Especificamos nuestras credenciales. Hemos de recordar que si estamos usando el **Learner Lab**, tendremos que definir el token de sesión.
AWS_ACCESS_KEY = 'ASIAQLLZGTZ5D5LNQSYC'
AWS_SECRET_KEY = 'lOi54j/VYGt4+nSdK0yw/C4iHdkiTRREuHsum+ET'
AWS_SESSION_TOKEN = 'IQoJb3JpZ2luX2VjEOT//////////wEaCXVzLXdlc3QtMiJHMEUCIQDCd64vv3F16DFbIyi5slYJBaSgtr9uHvzSzKiFZEy6AAIgOrdEky3dzGQ65kUrU4Amu/dsGHglT24SlMBE+JgVgtkqqQIIrf//////////ARAAGgwwMjQ0MTMzODAyMTgiDAV0lDEN0QxcJYnG8Sr9AT4p9K+BHEG2cRLn7Be2/FtW/yCLGT1tjKQ8QRIoQCOoXgCHEUNkee+i/gh1eKl9ZizZV5e+OSFpknCX1egBGTAgHQo3AgFUy0/fX/xWJ3Xtp/ryx3MSjPJNEUDh/ShUj3vDe29P+AosnRwKo6fsrQPCyCi1BGtHx5l2f+7RS2sTY/JK8SOaK/anx5U/lJrNwZgWeCIiqKejnwv9Qc+fXpIAyrqZkzaqSoUTeC4/S0yGMl5rVyr+7AFptyT8URmD2ca+8XNwmevDEVmWhmRiK4jMamV+PZXQwYxnSFHhfE4KtOI8FooXNTyeftQC+nUJGQdXeQA5KbjK9u6ZHAswofqzyAY6nQEDr9/0OaY7HpDv0CgSlPahPQjA3xoMa4KSzxp0tIdeDUYfzsSJ3KtjEnG5t9YSeMlFKB6gBhiy2RPB14QmWLtEJlC4LTINahhYbIvUnpcxTeRcoD04B2zeidEnrlmzI1XkebztxClHUcRn0wWcUCvgVKsdlFjeZ+YMdEtKo29pOekN+7JSuaiMTZGhjvnssdiCB/QSf6nU+dfrVvYu'
REGION = 'us-east-1'  # Cambia a la región donde tienes habilitado Rekognition

rekognition_client = boto3.client(
    'rekognition',
    region_name=REGION,  # Cambia esto a la región que estés usando
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    aws_session_token=AWS_SESSION_TOKEN  # Solo si tienes un token de sesión
)


# <h4 style="color:orange;">Paso 2. Leemos el fichero con el que queremos trabajar</h4>

# In[4]:


# Leemos la imagen desde el archivo en formato binario

IMAGE_FILE_PATH = "C:\\Users\\Administrador\\Documents\\carlos\\IABD--programacion-inteligencia-artificial\\Ejercicios\\Tarea-AWS\\imagenes\\cara1descarga.jpg"
with open(IMAGE_FILE_PATH, 'rb') as image_file:
    image_bytes = image_file.read()


# <h4 style="color:orange;">Paso 3. Realizamos la solicitud a DETECT_FACES</h4>

# In[5]:


# Realizar la solicitud DetectFaces al servicio de Rekognition
response = rekognition_client.detect_faces(
    Image={'Bytes': image_bytes},
    Attributes=['ALL']  # Especificamos que queremos todos los atributos (género, emociones, edad, etc.)
)


# <h4 style="color:orange;">Paso 4. Procesamos la respuesta</h4>

# La variable **response** que devuelve el método **detect_faces** de boto3 es un **diccionario** de Python. Boto3 convierte automáticamente las respuestas de AWS en diccionarios, que son estructuras de datos nativas en Python y muy similares a los objetos JSON. Estos diccionarios se pueden manejar directamente en Python sin necesidad de realizar ninguna conversión adicional para acceder a sus valores.

# In[6]:


print(response)


# In[7]:


# Si quiero mostrar cuáles son las claves de las entradas de primer nivel del diccionario que devuelve detect_faces:
response.keys()


# Es decir, sólo tiene una entrada llamada FaceDetails con toda la información devuelta.

# In[8]:


# Si ahora quiero recorrerme todas las entradas que tiene FaceDetails
face_details = response['FaceDetails']   # Guardo en esta variable todo el contenido de la entrada del diccionario

# Recorremos las distintas caras que se encuentran en face_details 
for i, face in enumerate(face_details):
    print(f"--- Información de la cara {i + 1} ---")
    
    # Rango de edad
    age_range = face['AgeRange']
    print(f"Rango de Edad: {age_range['Low']} - {age_range['High']}")

    # Género
    gender = face['Gender']['Value']
    print(f"Género: {gender}")

    # Emociones detectadas (puede haber más de una)
    print("Emociones detectadas:")
    for emotion in face['Emotions']:
        print(f"  {emotion['Type']}: {emotion['Confidence']:.2f}%")

    # Confianza general de la detección
    print(f"Confianza en la detección de la cara: {face['Confidence']:.2f}%\n")


# 
