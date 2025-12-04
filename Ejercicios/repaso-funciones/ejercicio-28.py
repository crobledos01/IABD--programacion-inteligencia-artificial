numero = int(input("Introduce la cantidad de números a sacar: "))

print("Los primeros", numero, "cuadrados perfectos son: ")
for i in range(1, numero + 1):
    print(i ** 2, end=", ")