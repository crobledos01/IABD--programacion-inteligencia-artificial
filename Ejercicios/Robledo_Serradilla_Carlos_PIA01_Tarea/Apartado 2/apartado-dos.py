# Problema 2. Frecuencia de palabras en un texto.
#  Escribe un programa que pida al usuario ingresar una frase o párrafo. Luego, el
#  programa debe contar cuántas veces aparece cada palabra en el texto y
#  mostrar las palabras junto con su frecuencia.
# Requisitos:
#  1. Eliminar los signos de puntuación y convertir todas las palabras a minúsculas para evitar diferencias.
#  2. Usar un diccionario donde la clave sea la palabra y el valor sea su frecuencia.
#  3. Mostrar las palabras y sus frecuencias de forma ordenada por la palabra.

import string
import unicodedata

texto = input('Introduce un texto: ').lower()
texto_normalizado = ''.join((texto for texto in unicodedata.normalize('NFD', texto) if unicodedata.category(texto) != 'Mn' and texto not in string.punctuation))

palabras = sorted(texto_normalizado.strip().split(' '))

diccionario = {}

for palabra in palabras:
    if palabra in diccionario: diccionario[palabra] = diccionario[palabra] + 1
    else: diccionario[palabra] = 1

print(diccionario)