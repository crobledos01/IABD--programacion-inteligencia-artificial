# Se importa exp de la librería math y se añaden los valores planteados en el ejercicio
from math import exp
lista1 = [-3, -6, -9, -12, -15]
lista2 = [-18, 15, 12, 9, 6, 3]
lista3 = [2, 3, 4, 5, 6, 7, 8]
dic = {1:lista1, 2:lista2, 3:lista3}


'''      
Esta función sirve para devolver la distancia recorrida en un día
Parameters:
------------
x (int): es el número del que se quiere calcular la función, procedente de las listas del diccionario

Returns: devuelve el resultado de la función en base al valor de x
---------
x: -3
return: exp(-3) / (-3 - 1) ** 2 = 0.049787068367863944
x: 3
return: exp(3) / (3 - 1) = 10.042768900219566
'''
def funcionX(x):
    if x > 1:
        return exp(x) / (x - 1)
    elif x < 1:
        return exp(x) / (x - 1) ** 2
    else:
        return 0

# Se crea una lista utilizando una comprensión que incluye:
## El resultado de la función para cada valor de las listas del diccionario, basándose en el nombre de la lista para crear otra lista resultado
## Un bucle que recorre por separado cada una de las listas que contiene el diccionario
## Una condición que filtra por el resultado de la función
## Otro bucle que recorre cada nombre y valor de las listas
resultado = {
    i: list(
        r for v in lista
        if (r := funcionX(v)) > 0.5
    )
    for i, lista in dic.items()
}

# Se imprime el resultado
print(resultado)