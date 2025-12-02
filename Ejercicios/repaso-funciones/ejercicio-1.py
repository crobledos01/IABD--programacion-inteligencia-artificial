n = int(input("Introduce el rango: "))
suma = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        suma += i

print("La suma de los números pares entre 1 y", n, "es:", suma)