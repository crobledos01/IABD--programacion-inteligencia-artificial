# Se pide al usuario un número y se crea una lista para meter sus divisores
numero = int(input("Introduce un número entre el 1 y el 300: "))
# Se comprueba que el número esté en el abanico indicado
if numero >= 1 and numero <= 300:
    # Para dar el resultado final, se utiliza la compresión que se compone de dos partes
    ## Se utiliza un bucle for para recorrer desde el número 1 hasta el número indicado
    ## La condición hacer que solo se añadan a la lista los números que dan como resto 0 al dividirlos entre el número indicado por el usuario
    divisores = [n for n in range(1, numero + 1) if numero % n == 0]
    # Se imprime el resultado
    print(f"Los divisores de {numero} son: ", end="")
    print(divisores)
# En caso de que no cumpla la condición, se le indica al usuario
else:
    print("El número introducido no está entre 1 y 300.")