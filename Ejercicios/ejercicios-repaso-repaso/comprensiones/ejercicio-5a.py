# Se define una tupla con los números indicados y una lista para almacenar el resultado
tupla = (3, 5, 7, 11)
resultado = []
# Se recorren los elementos con tres bucles anidados para generar todas las combinaciones
for i in tupla:
    for j in tupla:
        for k in tupla:
            # Se añade la tupla resultante a la lista
            resultado.append((i, j, k))
# Se imprime la lista con todas las combinaciones generadas
print(resultado)