# Se crea una lista con las bombas y se pide al usuario un string de números para comprobar sus posiciones
lista_con_bombas=[11, 107, 17, 67, 99, 45, 37, 87, 1007, 2007, 2027, 10007, 7, 1, 15, 81, 91, 88, 307]
texto_numeros = input("Introduce la lista de números que quieras introducir separados por espacios: ")
# Se realiza un try-catch para que, si el jefe ha puesto un caracter no numérico, salga del programa y le advierta sin dar error
try:
    # Se transforma el string primero en un array de string, se crea otra lista para añadirlos números
    # y se hace un bucle del array de textos para transformar cada valor a numérico y añadirlos a la lista
    numeros_string = texto_numeros.split(" ")
    numeros = []
    for s in numeros_string:
        numeros.append(int(s))
    # Se crea una variable bomba_encontrada con False por defecto para advertir al usuario de que no hay bombas si no se encuentra ninguno
    bomba_encontrada = False
    #Se crea un bucle que lee la lista de bombas. Se recorre la lista de bombas, porque necesitas saber la posición en la que se encuentran en la lista,
    # utilizando enumerate para poder comprobar el index, y para que no se repita un mensaje si el jefe ha añadido dos veces un número que sea una bomba
    for index, b in enumerate(lista_con_bombas):
        # Se comprueba que la bomba esté en la lista del jefe y, en caso positivo,
        # se pone la variable bomba_encontrada a True y se avisa del número y la posición de la bomba 
        if b in numeros:
            bomba_encontrada = True
            print(f"El número {b} era una bomba encontrada en la posición {index + 1}")
    # Si después de recorrer el bucle bomba_encontrada sigue a false, se avisa de que no se ha encontrado ninguna bomba
    if not bomba_encontrada:
        print("No se ha encontrado ninguna bomba. La lista es segura")
# Si el jefe ha introducido un caracter no numérico, salta la excepción y lanza el siguiente mensaje
except:
    print("Uno de los valores introducidos no era un número")