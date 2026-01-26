# Se crean las dos tuplas y una lista con las combinaciones de ambas
tupla1 = (7, 2)
tupla2 = (7, 8)
lista_combinaciones = []
# Se hacen dos bucles anidados, uno que contiene todas las combinaciones que empiecen con los números de la primera tupla y otro con los de la segunda.
# En cada recorrido del bucle interior de cada uno, se añaden las combinaciones dentro de una lista
for i in tupla1:
    for j in tupla2:
        lista_combinaciones.append((i, j))
for i in tupla2:
    for j in tupla1:
        lista_combinaciones.append((i, j))
# Se imprime por consola la lista con todas las combinaciones
print(f"Lista con repetidos: {lista_combinaciones}")
# Se crea una nueva lista para sacar solo los no repetidos
lista_sin_repetidos = []
# Se recorre la lista de combinaciones y, por cada vuelta, se comprueba si esa combinación ya se ha dado o no y se añade a la nueva lista en caso de que no existiese
for tupla in lista_combinaciones:
    if tupla not in lista_sin_repetidos:
        lista_sin_repetidos.append(tupla)
# Por último, se imprime esta nueva lista que no incluye repetidos
print(f"Lista sin repetidos: {lista_sin_repetidos}")