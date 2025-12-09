def normalizar_numeros(texto):
    texto = texto.replace(" ", "").split(",")
    return texto

def convertir_a_numero(textos):
    numeros = []
    for t in textos:
        n = int(t)
        numeros.append(n)
    return numeros

def son_anagramas(lista_1, lista_2):
    if len(lista_1) != len(lista_2):
        return False
    for i in range(0, len(lista_1)):
        if lista_1[i] != lista_2[i]:
            return False
    return True

texto_numeros_1 = input("Introduce la primera lista de números separados por comas: ")
lista_normalizada_1 = normalizar_numeros(texto_numeros_1)
lista_numerica_1 = convertir_a_numero(lista_normalizada_1)
lista_ordenada_1 = sorted(lista_numerica_1)

texto_numeros_2 = input("Introduce la segunda lista de números separados por comas: ")
lista_normalizada_2 = normalizar_numeros(texto_numeros_2)
lista_numerica_2 = convertir_a_numero(lista_normalizada_2)
lista_ordenada_2 = sorted(lista_numerica_2)

if son_anagramas(lista_ordenada_1, lista_ordenada_2):
    print("Las listas son anagramas")
else:
    print("Las listas no son anagramas")

