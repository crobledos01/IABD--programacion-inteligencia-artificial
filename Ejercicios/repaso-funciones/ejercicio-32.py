import math

def imprimir(numeros):
    for index, n in enumerate(numeros):
        if index != 0:
            print(end=", ")
        print(n, end="")

def criba(n):
    limite = math.ceil(n ** 0.5)
    numeros = []
    for i in range(2, n + 1):
        numeros.append(i)

    for i in range(2, limite):
        for j in range(i + i, n + 1, i):
            if j in numeros:
                numeros.remove(j)
    
    imprimir(numeros)


n = int(input("Introduce el número límite: "))
criba(n)