import random

lista = []
for index in range(10):
    lista.append(random.randint(1, 10))

for i in lista:
    print("Número:", i, "Cuadrado:", i**2, "Cubo:", i**3)