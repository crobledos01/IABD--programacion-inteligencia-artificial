def imprimir_divisores(numero):
    print("Los divisores de", numero, "son: ")
    for i in range (1, numero):
        if numero % i == 0:
            print(i)

numero = int(input("Introduce un número: "))
imprimir_divisores(numero)