class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print('El perro hace "Guau"')
        
class Gato(Animal):
    def hacer_sonido(self):
        print('El perro hace "Miau"')

perro = Perro()
perro.hacer_sonido()

gato = Gato()
gato.hacer_sonido()