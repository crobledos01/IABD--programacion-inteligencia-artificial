def generarTabla(numero):
    for i in range(1, 11):
        print(numero, "*", i, "=", numero * i)

numero = int(input("Introduce un número: "))
generarTabla(numero)