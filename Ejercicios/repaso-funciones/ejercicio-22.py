def esPrimo(numero):
    for i in range (2, numero):
        if numero % i == 0:
            return False
        
    return True

def sumarPrimos(numero):
    suma = 0
    for i in range(2, numero + 1):
        if esPrimo(i):
            suma = suma + i
    return suma

numero = int(input("Introduce el número límite para la suma: "))

print("La suma de los números primos hasta el", numero, "es: ", sumarPrimos(numero))