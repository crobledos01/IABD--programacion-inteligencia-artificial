'''      
Esta función sirve para validar que la lista de números no esté vacía antes de calcular el promedio
Para ello, llama a una función anterior que contiene la lista como parámetro, y si la lista está vacía, lanza un error
Parameters:
------------
lista (array): es la lista de números de la que se quiere calcular el promedio

Returns: devuelve la lista si no está vacía
---------
lista: [1, 3, 5, 7, 9]
return: [1, 3, 5, 7, 9]

lista: []
return: ValueError: La lista no puede estar vacía
'''
def validar_lista_no_vacia(func):
    def validacion(lista):
        if not lista:
            raise ValueError("La lista no puede estar vacía")
        return func(lista)
    return validacion

'''      
Esta función sirve para devolver el promedio en una lista denumeros.
Para ello, utiliza validar_lista_no_vacia como decorador para asegurarse de que la lista no esté vacía
Parameters:
------------
lista (array): es la lista de números de la que se quiere calcular el promedio

Returns: devuelve el resultado de la división entre la suma de los números y la longitud de la lista
---------
lista: [1, 3, 5, 7, 9]
return: 25 / 5 = 5.0
'''
@validar_lista_no_vacia
def promedio(lista):
    return sum(lista) / len(lista)

# Para probar, se crea una matriz con varias listas y se recorren con un bucle para llamara a la función con cada una de ellas
# Las dos primeras listas devolveran el promedio, mientras que la última lanzará un error tras imprimir el primer texto
pruebas = [[1, 3, 5, 7, 9], [5], []]
for lista in pruebas:
    print(f"Prueba con la lista {lista}")
    print(promedio(lista))