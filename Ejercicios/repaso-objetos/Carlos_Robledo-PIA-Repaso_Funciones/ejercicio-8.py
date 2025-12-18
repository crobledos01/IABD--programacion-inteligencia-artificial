#Se crea la clase animal y se le mete la función hacer_sonido con un pass dentro para que se salga de la función
class Animal:
    def hacer_sonido(self):
        pass

#Se crea la subclase perro procedente de animal y se actualiza hacer_sonido para que ladre
class Perro(Animal):
    def hacer_sonido(self):
        print('El perro hace "Guau"')
        
#Se crea la subclase gato procedente de animal y se actualiza hacer_sonido para que maulle
class Gato(Animal):
    def hacer_sonido(self):
        print('El perro hace "Miau"')

#Se crea un perro y se llama a su función de sonido
perro = Perro()
perro.hacer_sonido()

#Se crea un gato y se llama a su función de sonido
gato = Gato()
gato.hacer_sonido()