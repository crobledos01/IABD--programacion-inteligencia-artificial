# Se hace una lista para los números y otra para el resultado de hacer el cubo de estos
lista_numeros = [2, 4, 8, 16]
lista_cubos = []
# Se recorre la primera lista y se añade a la segunda el cubo de cada número
for n in lista_numeros:
    lista_cubos.append(n ** 3)
# Se utiliza zip para agrupar las dos listas en una tupla y se imprime
tupla = zip(lista_numeros, lista_cubos)
list(tupla)