def contar_palabras(cadena):
    palabras = cadena.split(" ")
    print(len(palabras))

cadena = input("Introduce una cadena de texto: ")
contar_palabras(cadena)