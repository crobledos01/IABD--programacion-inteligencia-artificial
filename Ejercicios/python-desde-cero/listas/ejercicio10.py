import random

tabla = []
for i in range(1, 6):
    fila = []
    for j in range(1, 6):
        fila.append(random.randint(1, 50))
    tabla.append(fila)

print("Números generados: ")
for fila in tabla:
    print()
    for numero in fila:
        print(numero, end="\t")

print("\nSuma por fila: ")
for i in range(len(tabla)):
    print("Fila", i + 1, ": ", sum(tabla[i]))

print("Suma por columna: ")
for i in range(len(tabla[0])):
    suma_columna = 0
    for j in range(len(tabla)):
        suma_columna += tabla[j][i]
    print("Columna", i + 1, ": ", suma_columna)