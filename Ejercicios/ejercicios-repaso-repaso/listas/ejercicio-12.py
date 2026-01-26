# Se crea una lista de listas con valores numéricos, se pide al usuario el número que
# se busca (K) y las veces que debe aparecer(N) y se crea una lista para meter los resultados
listas = [[1, 2, 2, 3, 2, 3, 3, 1], [1, 2, 2, 3, 4, 1], [1, 2, 2, 2], [1, 2, 3, 4, 5]]
K = int(input("Introduce el número a buscar: "))
N = int(input("Introduce las veces que se tiene que repetir el número: "))
lista_salida = []
# Se crea un bucle que cuenta si en cada lista interior aparece el número con su cantidad y, en caso de que cumpla la condición, se añade a los resultados
for lista in listas:
  if lista.count(K) == N:
    lista_salida.append(lista)
# Si no existen conicidencias se avisa al usuario y si existen se imprimen
if len(lista_salida) == 0:
  print(f"No hay listas que en las que el número {K} aparezca {N} veces")
else:
  print(f"Las listas en las que {K} aparece {N} veces son: ")
  print(lista_salida)