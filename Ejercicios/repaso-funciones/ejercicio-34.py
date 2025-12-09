import string

def normalizar_cadena(cadena):
    cadena = cadena.replace(" ", "").upper()
    cadena_normalizada = ""
    for car in cadena:
        if car not in string.punctuation:
            cadena_normalizada = cadena_normalizada + car
    return cadena_normalizada

def diccionario(cadena):
    
    diccionario = {}
    for car in cadena:
        if car in diccionario:
            diccionario[car] = diccionario[car] + 1
        else:
            diccionario[car] = 1
    return diccionario

cadena = input("Introduce una cadena: ")
cadena_normalizada = normalizar_cadena(cadena)
diccionario_letras = diccionario(cadena_normalizada)

print(diccionario_letras)