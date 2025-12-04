def calcular_multiplos(numero):
    print("Los múltiplos de 3 y 5 hasta el", numero, "son: ")
    for i in range(1, numero + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i, end=", ")


numero = int(input("Introduce el número límite para el cálculo: "))

calcular_multiplos(numero)