# Se crea un array que contiene las filas y las columnas de un tablero de ajedrez. Para ello, de arriba a abajo:
## Se junta la letra de la columna con el número de la fila, que se debe convertir a string
## Se realiza un bucle que recorre cada letra de las columnas del tablero
## Se realiza otro bucle exterior que recorre los números de las filas del tablero
tablero_ajedrez = [
    [
        c + str(f)
        for c in 'abcdefgh'
    ]
    for f in range(8, 0, -1)
]
# Se crea un bucle para mostrar el tablero separando las filas por líneas
for f in tablero_ajedrez:
    print(f)