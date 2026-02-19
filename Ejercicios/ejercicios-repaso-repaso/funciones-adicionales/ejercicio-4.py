# Encuentra el número perdido en una secuencia aritmética dada como lista separada por comas
def encontrar_perdido(lista):
    # Convierte la cadena en una lista de enteros
    lista_num = [
        int(n)
        for n in lista.split(",")
    ]
    cantidad = len(lista_num)
    # Calcula la diferencia común de la progresión
    diferencia = (lista_num[-1] - lista_num[0]) // cantidad

    # Busca el valor que falta en la secuencia
    for i in range(1, cantidad):
        esperado = lista_num[i-1] + diferencia
        if lista_num[i] != esperado:
            return esperado

# Solicita la lista al usuario y muestra el número perdido
lista = input("Introduce una lista de números separados solo por comas:")
print("El número perdido es:", encontrar_perdido(lista))