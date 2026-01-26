# Se pide al usuario los números, se divide la cadena que se recibe para tener una lista y se crea otra para guardar los resultados
cadena_numeros = input("Introduce una lista de números separados por espacios: ")
lista_numeros = cadena_numeros.split(" ")
lista_3_apariciones = []
# Se crea un bucle que comprueba si el número aparece tres veces y que no está ya en la lista y, si ambas cosas se cumplen, se añade
for n in lista_numeros:
  if lista_numeros.count(n) == 3 and n not in lista_3_apariciones:
    lista_3_apariciones.append(n)
# Si no hay números en la lista se avisa al usuario y, si encuentra resultados, se imprimen utilizando un bucle para imprimirlos
if len(lista_3_apariciones) == 0:
  print("No hay números que se repitan 3 veces")
else:
  print("Los números que se repiten 3 veces son: ", end="")
  for index, n in enumerate(lista_3_apariciones):
    if index != 0:
      print(end=", ")
    print(n, end="")
