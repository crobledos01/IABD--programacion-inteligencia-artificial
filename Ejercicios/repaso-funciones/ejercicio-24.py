def espacio_inicial(filas, actual):
    if filas > 5 and actual < 5:
        print(end=" ")
    for i in range(0, (filas - actual)):
        print(end="  ")

def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    factorial = 1
    for n in range(1, numero + 1):
        factorial = factorial * n

    return factorial

def coef_binomial(n, k):
    dividendo = factorial(n)
    divisor = factorial(k) * factorial(n-k)
    coeficiente = dividendo / divisor
    return coeficiente

def triangulo_pascal(filas):
    for i in range(0, filas):
        fila = []
        for j in range(0, i + 1):
            fila.append(coef_binomial(i, j))

        print("")
        
        espacio_inicial(filas, i)

        for j in range(0, len(fila)):
            print(fila[j], end=" ")

filas = int(input("Introduce el número de filas: "))
triangulo_pascal(filas)