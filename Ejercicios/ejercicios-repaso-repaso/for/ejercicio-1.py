# Se pide la lista de números y se utiliza split para separarlos por espacios en una lista en la que continuan siendo textos
texto_numeros = input("Introduce una lista de números separados por un espacio: ")
lista_numeros = texto_numeros.split(" ")
for t in lista_numeros:
    # Se transforma el número, que seguía en tipo string, a int
    numero = int(t)
    # Se calcula el resto del número entre 2 para comprobar que, si el resto es 0, el número es par
    if numero % 2 == 0:
        # Si el resto es cero, imprime el número y fuerza la salida del for con un break, saltándose el else
        print(f"El primer número par de la lista es el {numero}")
        break
#Si llega al else es porque no ha saltado el break y, por tanto, no ha encontrado resultados.
else:
    print("No se han encontrado números pares")