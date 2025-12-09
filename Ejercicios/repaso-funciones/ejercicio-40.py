def sumar_numeros(matriz):
    suma = 0
    for fila in matriz:
        for numero in fila:
            suma = suma + numero
    return suma


print("Introduce los números de una matriz 5x5 de uno en uno: ")
matriz = []
for i in range(0, 5):
    fila = []
    for j in range(0, 5):
        fila.append(int(input(f"Introduce la posición {i + 1}-{j + 1}: ")))
    matriz.append(fila)

print("Tu matriz es la siguiente: ")
for fila in matriz:
    print(fila)

print("La suma de sus dígitos es: ", sumar_numeros(matriz))