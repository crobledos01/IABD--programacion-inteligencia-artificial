# Se crea una matriz con los elementos a buscar
matriz = [[1, 2, 2, 4, 3, 6],[5, 1, 3, 4],[9, 5, 7, 1],[2, 4, 1, 3]]
# Se genera un set que los contenga
elementos = set()
# El bucle anidado divide primero por listas dentro de la matriz y después en elementos dentro de cada lista
for lista in matriz:
    for e in lista:
        # Se añade cada elemento al set. En caso ya existir, este no se duplica
        elementos.add(e)
# Se ordena el set de elementos y se imprime
elementos = sorted(elementos)
print(f"Los elementos ordenados que aparecen son: {elementos}")