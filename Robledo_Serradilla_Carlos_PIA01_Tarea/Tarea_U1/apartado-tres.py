# Problema 3. Intersección y unión de conjuntos
#  Escribe un programa que permita al usuario crear dos conjuntos de números
#  enteros. Luego, el programa debe calcular y mostrar:
#  1. La intersección de ambos conjuntos (elementos comunes).
#  2. La unión de ambos conjuntos (todos los elementos sin duplicados).
#  3. La diferencia simétrica (elementos que están en uno u otro conjunto, pero no en ambos).

input_uno = input('Añade la primera lista con los números separados por espacios: ').strip().split(' ')
input_dos = input('Añade la segunda lista con los números separados por espacios: ').strip().split(' ')

lista_uno = [int(n) for n in input_uno]
lista_dos = [int(n) for n in input_dos]

lista_comun = [n for n in input_uno if n in input_dos]
lista_total = [n for n in input_uno] + [m for m in input_dos if m not in input_uno]
lista_simetrica = [n for n in input_uno if n not in input_dos] + [n for n in input_dos if n not in input_uno]

print('Lista común: ' + str(lista_comun))
print('Lista total: ' + str(lista_total))
print('Lista simétrica: ' + str(lista_simetrica))