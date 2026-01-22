# Se pide la lista de nombres y se utiliza split para separarlas por espacios en una lista
texto_nombres = input("Introduce una lista de nombres separados por un espacio: ")
lista_nombres = texto_nombres.split(" ")
# Se hace un bucle por cada nombre
for n in lista_nombres:
    # Se coge el primer carácter del nombre, se utiliza upper para contemplar los casos en minúsculas y se compara con la letra A
    if n[0].upper() == "A":
        # Si comienza con la letra A, imprime el nombre y fuerza la salida del for con un break, saltándose el else
        print(f"El primer nombre que empieza por A de la lista es {n}")
        break
#Si llega al else es porque no ha saltado el break y, por tanto, no ha encontrado resultados.
else:
    print("No se han encontrado nombres que empiecen por A")