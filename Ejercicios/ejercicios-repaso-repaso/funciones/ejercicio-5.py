# Se añaden los valores planteados en el ejercicio
distancias_diarias = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
altura_muro = 125
caida_nocturna = 20
total_distancia_recorrida = 0
dias = 0

'''      
Esta función sirve para devolver la distancia recorrida en un día
Parameters:
------------
total (str): es el total avanzado hasta ese momento
distancias (array): es la lista de distancias que recorre al día
dias (int): es el día en el que se encuentra

Returns: devuelve el total avanzado tras ese día
-----------
index (int): devuelve la posición real del día en el array
Examples:
---------
total: 33
distancias: [53, 21, 7]
dia: 2
index : 2 - 1 = 1
return = 33 + 21 = 54
'''
def avance(total, distancias, dia):
    index = dia - 1
    return total + distancias[dia]

'''      
Esta función sirve para comprobar si el caracol ha llegado a la cima
Parameters:
------------
total (str): es el total avanzado hasta ese momento
altura (int): es la altura todal de la pared en cm

Returns: devuelve True/False en función de si el caracol ha llegado a la cima
-----------
Examples:
---------
total: 33
altura: 125
return False

total: 133
altura: 125
return True
'''
def comprobar_fin(total, altura):
    return total >= altura

# Se realiza un bucle que hará que avancen los días hasta que comprobar_fin devuelva true
while not comprobar_fin(total_distancia_recorrida, altura_muro):
    # Se añade un día y se llama a la función avance para sumar la altura que recorre ese día al total
    dias = dias + 1
    total_distancia_recorrida = avance(total_distancia_recorrida, distancias_diarias, dias)
    # Si tras llamar de nuevo a comprobar_fin no ha llegado a la cima, se le resta la distancia de caída de la noche
    if not comprobar_fin(total_distancia_recorrida, altura_muro):
        total_distancia_recorrida -= caida_nocturna

# Se imprime el resultado
print(f"El caracol ha tardado {dias} días en subir la pared")
