def mayor(lista):
    lista.sort(reverse=True)
    return lista[0]

numeros = [1, 6, 6, 3, 7, 8, 4, 8, 6, 6, 2, 7, 5, 9, 1, 9, 5, 3, 1, 7, 0, 5]

print("El número mayor es: ", mayor(numeros))