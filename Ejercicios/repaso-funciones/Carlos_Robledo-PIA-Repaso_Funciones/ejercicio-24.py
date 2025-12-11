#Esta función es solo para darle forma al triángulo
def espacio_inicial(filas, actual):
    if filas > 5 and actual < 5:
        print(end=" ")
    for i in range(0, (filas - actual)):
        print(end="  ")

#Se calcula el factorial de cada uno de los números que se envian al coeficiente
def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    factorial = 1
    for n in range(1, numero + 1):
        factorial = factorial * n

    return factorial

#Se calcula el coeficiente binomial de los números correspondientes a la posición y la fila por la que está imprimiéndose el triángulo
def coef_binomial(n, k):
    dividendo = factorial(n)
    divisor = factorial(k) * factorial(n-k)
    coeficiente = dividendo / divisor
    return coeficiente

#Imprime el triángulo de Pascal.
#Al mandarle el número de filas, lo primero que se hace es un bucle con la cantidad indicada
#Dentro, se hace un nuevo bucle que servirá para meter los números en cada fila, este coge un número más por cada fila ya realizada y realiza el coeficiente de cada fila y valor
#Por último, se imprime fila por fila para formar la pirámide (después de llamar a la función que le da forma)
def triangulo_pascal(filas):
    for i in range(0, filas):
        fila = []
        for j in range(0, i + 1):
            fila.append(coef_binomial(i, j))

        print("")
        espacio_inicial(filas, i)

        for j in range(0, len(fila)):
            print(fila[j], end=" ")

#Se pide el número por consola y se llama a la función
filas = int(input("Introduce el número de filas: "))
triangulo_pascal(filas)