def normalizar_numeros(texto):
    texto = texto.replace(" ", "").split(",")
    return texto

def convertir_a_numero(textos):
    numeros = []
    for t in textos:
        n = int(t)
        numeros.append(n)
    return numeros

def es_orden_ascendente(numeros):
    for i in range(1, len(numeros)):
        if i != 0:
            if numeros[i] < numeros[i - 1]:
                return False
    return True

texto_numeros = input("Introduce una lista de números separados por comas: ")
lista_normalizada = normalizar_numeros(texto_numeros)
lista_numerica = convertir_a_numero(lista_normalizada)
esta_ordenada = es_orden_ascendente(lista_numerica)

if esta_ordenada:
    print("La lista está ordenada ascentendetente")
else:
    print("Las lista no está ordenada ascendentemente")