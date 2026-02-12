def encontrar_perdido(lista):
    cantidad = len(lista)
    diferencia = (lista[-1] - lista[0]) // cantidad

    for i in range(1, cantidad):
        esperado = lista[i-1] + diferencia
        if lista[i] != esperado:
            return esperado

