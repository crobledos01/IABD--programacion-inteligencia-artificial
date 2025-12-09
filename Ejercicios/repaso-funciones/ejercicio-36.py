def normalizar_numeros(texto):
    texto = texto.replace(" ", "").split(",")
    return texto

def convertir_a_numero(textos):
    numeros = []
    for t in textos:
        n = int(t)
        numeros.append(n)
    return numeros

def comprobar_duplicados(numeros):
    duplicados = []
    for indexI, i in enumerate(numeros):
        for indexJ, j in enumerate(numeros):
            if indexI != indexJ and i == j and i not in duplicados:
                duplicados.append(i)
                break
    return duplicados

texto_numeros = input("Introduce una lista de números separados por comas: ")
lista_normalizada = normalizar_numeros(texto_numeros)
lista_numerica = convertir_a_numero(lista_normalizada)
duplicados = comprobar_duplicados(lista_numerica)

if len(duplicados) == 0:
    print("No hay ningún número duplicado en la lista")
else:
    print("Los siguientes números están duplicados: ",end="")
    for index, i in enumerate(duplicados):
        if index != 0:
            print(end=", ")
        print(i, end="")