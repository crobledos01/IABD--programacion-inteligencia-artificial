def obtener_divisores(numero):
    divisores = []
    print("Los divisores de", numero, "son: ")
    for i in range (1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

numero = int(input("Introduce un número: "))
divisores = obtener_divisores(numero)

suma_divisores = sum(divisores)

if numero == suma_divisores:
    print("El número", numero, "es perfecto")
else:
    print("El número", numero, "no es perfecto")