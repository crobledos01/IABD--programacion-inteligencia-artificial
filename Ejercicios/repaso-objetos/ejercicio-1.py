class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

def saludar(perrete):
    print("Hola", perrete.nombre)

nombre = input("Introduce el nombre del perro: ")
edad = int(input("Introduce la edad del perro: "))

perrete = Perro(nombre, edad)

saludar(perrete)