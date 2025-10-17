# Problema 1. División de una lista de enteros.
#  Escribe una función que reciba por parámetro una lista de enteros y devuelva
#  dos listas: una con los valores negativos que tuviera y otra con los positivos.
#  Ambas listas deben estar ordenadas ascendentemente

lista_numeros = [1, 4, -12, 7, -4, 8, -124, 51, 2]

lista_positivos = [numero for numero in lista_numeros if numero > 0]
lista_negativos = [numero for numero in lista_numeros if numero < 0]

print('Números positivos: ' + str(sorted(lista_positivos)))
print('Números negativos: ' + str(sorted(lista_negativos)))