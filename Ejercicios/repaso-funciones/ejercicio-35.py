def normalizar_numeros(texto):
    texto = texto.replace(" ", "").split(",")
    return texto

def convertir_a_numero(textos):
    numeros = []
    for t in textos:
        n = int(t)
        numeros.append(n)
    return numeros
    
def promedio(numeros):
    suma = 0
    for i in numeros:
        suma = suma + i
    return suma / len(numeros)

texto_numeros = input("Introduce una lista de números separados por comas: ")
lista_normalizada = normalizar_numeros(texto_numeros)
lista_numerica = convertir_a_numero(lista_normalizada)
promedio = promedio(lista_numerica)

print("El promedio de los números es:", promedio)