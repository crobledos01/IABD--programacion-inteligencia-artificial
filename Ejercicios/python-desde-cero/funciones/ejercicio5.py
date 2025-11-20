def calcularMinMax(numeros):
    numeros.sort()
    return {
        'min': numeros[0],
        'max': numeros[len(numeros) - 1]
    }

continuar = True
numeros = []
while continuar:
    try:
        numero = int(input("Introduce un número (o una letra para abandonar): "))
        numeros.append(numero)

    except:
        continuar = False

minMax = calcularMinMax(numeros)
print("El número mayor es", minMax['max'], "y el menor es", minMax['min'])