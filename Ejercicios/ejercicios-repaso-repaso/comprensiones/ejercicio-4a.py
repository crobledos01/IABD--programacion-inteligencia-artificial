# Se pide al usuario un número y se crea una lista para meter sus divisores
numero = int(input("Introduce un número entre el 1 y el 300: "))
divisores = []
# Se comprueba que el número esté en el abanico indicado
if numero >= 1 and numero <= 300:
    # Para comprobar los divisores, se recorre número por número hasta encontrar el indicado
    for n in range(1, numero + 1):
        # Si el resto del número indicado y el que recorre el array es 0, se añade a la lista de divisores
        if numero % n == 0:
            divisores.append(n)
    # Se imprime el resultado
    print(f"Los divisores de {numero} son: ", end="")
    print(divisores)
# En caso de que no cumpla la condición, se le indica al usuario
else:
    print("El número introducido no está entre 1 y 300.")