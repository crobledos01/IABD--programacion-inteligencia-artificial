class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def descripcion(self):
        print("El animal se llama", self.nombre)

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def maullar(self):
        print("MIAU")

nombre = input("Introduce el nombre del gato: ")

gato = Gato(nombre)
gato.descripcion()
gato.maullar()
