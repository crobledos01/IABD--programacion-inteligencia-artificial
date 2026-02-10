# Se importa random y se crea un array para guardar los números
import random as random
numeros = []
# Se realiza un bucle con 100.000 vueltas. Cada una generará un número del 1 al 6 y lo añadirá al array de números
for _ in range(100000):
    numeros.append(random.randint(1, 6))
# Se crea una variable par acontar las veces que aparece el número 6
contador = 0
# Se recorre el array de números y, si aparece el número 6, se suma uno al contador
for n in numeros:
    if n == 6:
        contador = contador + 1
# Se dividen las veces que ha aparecido el 6 entre los números totales y se multiplica por 100 para obtener un porcentaje
probabilidad = (contador / 100000) * 100
# Se imprime el resultado
print(f"La probabilidad de sacar un 6 es {probabilidad}%.")