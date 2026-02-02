# Se define la tupla con los elementos a combinar
tupla = (3, 5, 7, 11)
# Se usa una comprensión de listas para generar la unión anidando tres bucles
resultado = [(i, j, k) for i in tupla for j in tupla for k in tupla]
# Se imprime la lista resultante
print(resultado)