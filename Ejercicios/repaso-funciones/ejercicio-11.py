cantidad = int(input("Introduce la cantidad de números de la secuencia: "))
anterior = 0
ultimo = 1
for i in range(1, cantidad + 1):
    copia_ultimo = ultimo
    print(anterior, "+", ultimo, "=", end=" ")
    ultimo = anterior + ultimo
    anterior = copia_ultimo
    print(ultimo)
