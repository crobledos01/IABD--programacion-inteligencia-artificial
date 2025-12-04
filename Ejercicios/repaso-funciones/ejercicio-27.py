def esPrimo(numero):
    for i in range (2, numero):
        if numero % i == 0:
            return False
        
    return True

def sumarPrimos(numero):
    primos = []
    for i in range(2, numero + 1):
        if esPrimo(i):
            primos.append(i)
    return primos

numero = int(input("Introduce el número límite para buscar los números primos: "))

print("Los números primos del 2 al", numero, "son: ")
for i in sumarPrimos(numero):
    print(i, end=", ")

