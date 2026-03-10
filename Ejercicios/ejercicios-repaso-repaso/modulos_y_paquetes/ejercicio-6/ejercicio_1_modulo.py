import random

# Esta función genera una lista de 7 números aleatorios utilizando un bucle for y los devuelve al usuario
def generar_numeros_aleatorios():
    numeros = []
    for _ in range(7):
        numeros.append(random.randint(1, 100))

    return numeros

# Utilizando un bucle for, se imprimen los números de la lista separados por comas
def imprimir_numeros(numeros):
    for i, numero in enumerate(numeros):
        if i != 0:
                print(", ", end="")

        print(numero, end="")

    print()

# Esta función devuelve la lista con los números ordenados
def ordenar_numeros(numeros):
    return sorted(numeros)