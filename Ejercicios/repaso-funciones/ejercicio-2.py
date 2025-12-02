numeros = [1, 6, 6, 3, 7, 8, 4, 8, 6, 6, 2, 7, 5, 9, 1, 9, 5, 3, 1, 7, 0, 5]

numero = int(input("Introduce el número a buscar: "))

cantidad = 0

for i in numeros:
    if i == numero:
        cantidad = cantidad + 1

print("El número", numero, "aparece", cantidad, "veces")