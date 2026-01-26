# Se crea la lista que indica el ejercicio, se pide al usuario una cantidad y se crea una lista para guardar los resultados
L = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
K = int(input("Introduce un número: "))
numeros = []
# Se hace un bucle con los valores de la lista. Dentro, se comprueba quela cantidad de vecesque aparecesea mayor
# a la que indica el usuario y que no esté ya en la lista resultado. Si esto se cumple, se añade a la lista
for n in L:
  if L.count(n) > K and n not in numeros:
    numeros.append(n)
# Si no hay ningún resultado se imprime por pantalla un mensaje diciendo que no hay números y
# en caso de que si haya, se le indica al usuario creando un bucle para imprimirlos
if len(numeros) == 0:
  print(f"No hay números que aparezcan más de {K} veces")
else:
  print(f"Los números que aparecen más veces de {K} veces en la lista son: ", end="")
  for index, n in enumerate(numeros):
    if index != 0:
      print(end=", ")
    print(n, end="")