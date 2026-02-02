# Se importa el módulo array
from array import array
# Se crea un array y se pide al usuario el número
lista = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
numero = int(input("Introduce el número a eliminar: "))
# Si el número está en la lista, remove elimina la primera vez que lo encuentra y se imprime la lista
if numero in lista:
    lista.remove(numero)
    print(lista.tolist())
# Si el número no está en la lista, se avisa al usuario.
else:
    print("El número introducido no está en la lista")