# Se pide la lista de palabras y se utiliza split para separarlas por espacios en una lista
texto_palabras = input("Introduce una lista de palabras separados por un espacio: ")
lista_palabras = texto_palabras.split(" ")
# Se hace un bucle por cada palabra
for p in lista_palabras:
    #En las palabras, len cuenta la longitud de la palabra, se hace un if para contar las letras
    if len(p) >= 10:
        # Si tiene más de 10 letras, imprime la palabra y fuerza la salida del for con un break, saltándose el else
        print(f"La primera palabra con más de 10 letras es {p}")
        break
#Si llega al else es porque no ha saltado el break y, por tanto, no ha encontrado resultados.
else:
    print("No se han encontrado palabras que más de 10 letras")