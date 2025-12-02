import random

def numero_aleatorio(menor, mayor):
    return random.randint(menor, mayor)

menor = int(input("Introduce el número más najo que pueda resultar: "))
mayor = int(input("Introduce el número más alto que pueda resultar: "))

print("El número resultante es:", numero_aleatorio(menor, mayor))