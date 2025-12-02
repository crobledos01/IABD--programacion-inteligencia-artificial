numero = input("Introduce un número: ")

suma = 0
for n in numero:
    suma = suma + int(n)

print("La suma de los dígitos de", numero, "es:", suma)