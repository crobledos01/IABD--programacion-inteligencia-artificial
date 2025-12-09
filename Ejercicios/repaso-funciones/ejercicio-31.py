def normalizar_numeros(texto):
    texto = texto.replace(" ", "").split(",")
    return texto

def convertir_a_numero(textos):
    numeros = []
    for t in textos:
        n = int(t)
        numeros.append(n)
    return numeros

def ordenacion_burbuja(numeros):

    n = len(numeros)

    for i in range(n):

        intercambiado = False
        
        for j in range(0, n-i-1):
            if numeros[j] > numeros[j+1]:
                avanzar = numeros[j]
                numeros[j] = numeros[j+1]
                numeros[j+1] = avanzar
                intercambiado = True

        if not intercambiado:
            break

    return numeros
    
texto_numeros = input("Introduce una lista de números separados por comas: ")
lista_normalizada = normalizar_numeros(texto_numeros)
lista_numerica = convertir_a_numero(lista_normalizada)
lista_ordenada = ordenacion_burbuja(lista_numerica)

print("La lista de números ordenada es: ")
for index, n in enumerate(lista_ordenada):
    if index != 0:
        print(end=", ")
    print(n, end="")