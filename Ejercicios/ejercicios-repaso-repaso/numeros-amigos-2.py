# Calcula los divisores haciendo un bucle desde 1 hasta la mitad del número
# Añade a un array los que den 0 en el resto al dividir y al acabar devuelve los divisores
def calcDivisores(numero):
    divisores = []
    i = 1
    while i <= numero / 2:
        if numero % i == 0:
            divisores.append(i)
        i += 1
    return divisores

# Funcion para calcular los números amigos. num_busquedas es la cantidad de numeros en la que va a buscar si existen los números amigos suficientes
def buscar_numeros_amigos(cantidad):
    num_busquedas = 10000

    # Se hace un bucle while para repetir el bucle aumentando la cantidad de búsquedas en caso de que no sean suficientes
    # el array numeros_amigos es para guardar los que encuentre y suma_divisores_por_num es un array que contiene la suma de los divisores de la posición en la que se encuentra la suma
    while len(numeros_amigos) < cantidad:
        numeros_amigos = []
        suma_divisores_por_num = [0] * num_busquedas

        # Se hace un bucle desde el primer número hasta el número de búsqueda. En cada pasada del bucle calcula los divisores de un número,
        # calcula la suma de ellos y los añade al array suma_divisiones en la posición de dicho número
        for n in range(0, num_busquedas):
            divisores = calcDivisores(n)
            suma_divisores_por_num[n] = sum(divisores)
        
        # Se hace otro bucle para recoger el segundo número con el que comparar. Por cada pasada recoge los divisores y los suma
        for n in range(0, num_busquedas // 2 + 1):
            divisores = calcDivisores(n)
            sum_div = sum(divisores)

            # Se incluye otro for dentro del primero, en este, m corresponde a cada una de las posiciones del array suma_divisores_por_num,
            # después, se hace un if que compara que el primer número sea mayor que el segundo para no repetir, que los números sean distintos
            # y que los divisores de un número coincidan con el otro y viceversa. Por último, si todo esto se da, se añade al array de números amigos
            for m in range(0, num_busquedas + 1):
                if m > n and n != m and suma_divisores_por_num[m] == n and sum_div == m:
                    numeros_amigos.append((m, n))

        # Se añaden más números a la búsqueda por si se da el caso de que no son suficientes
        num_busquedas = num_busquedas + 10000

    # Devuelve la cantidad indicada de números amigos
    return numeros_amigos[:cantidad]

# Se pide la cantidad al usuario, se llama a la función para buscar números amigos junto con la cantidad indicada y se imprime el resultado
cantidad = int(input("Introduce la cantidad de números amigos a encontrar: "))
lista_na = buscar_numeros_amigos(cantidad)
print(f"Los primeras {cantidad} parejas de números amigos son: {lista_na}")