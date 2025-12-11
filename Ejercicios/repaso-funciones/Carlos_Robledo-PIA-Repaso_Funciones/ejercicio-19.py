#Se obtienen los divisores del número.
#Para esto, se divide el número entre todos los enteros en el rango del 1 al número y si el resto es 0 es que es divisor
def obtener_divisores(numero):
    divisores = []
    for i in range (1, numero):
        if numero % i == 0:
            divisores.append(i)
    print("Los divisores de", numero, "son:", divisores)
    return divisores

#Se pide el número por consola y se llama a la función
numero = int(input("Introduce un número: "))

divisores = obtener_divisores(numero)

#Se suman todos los divisores
suma_divisores = sum(divisores)

#Si ambos valores coinciden, el número es perfecto
if numero == suma_divisores:
    print("El número", numero, "es perfecto")
else:
    print("El número", numero, "no es perfecto")