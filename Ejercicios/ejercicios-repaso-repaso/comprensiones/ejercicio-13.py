# Para conseguir los números aleatorios es necesario importar el módulo random
import random as random
# Se piden al usuario las dimensiones de la matriz
filas = int(input("Introduce el número de filas de la matriz: "))
columnas = int(input("Introduce el número de columnas de la matriz: "))
# Se crea la matriz utilizando una comprensión que anida tres bucles:
## El más externo recorre las filas
## El intermedio recorre las columnas
## El más interno genera una lista con tres números aleatorios entre 0 y 255
matriz = [
        [
            [random.randint(0, 255) for _ in range(3)]
        for _ in range(columnas)]
    for _ in range(filas)
]
# Se muestra la matriz resultante utilizando un bucle para que las filas queden divididas
for fila in matriz:
    print(fila)