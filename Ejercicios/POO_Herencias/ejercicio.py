# Clase Mamifero
# Contiene las patas del animal y el color del pelaje
# Tiene dos métodos para indicar al usuario que el mamífero está amamantando a sus crías y que está durmiendo
class Mamifero:
    def __init__(self, patas:int, pelaje:str):
        self.patas = patas
        self.pelaje = pelaje
    
    def amamantar(self):
        print("El mamifero está amamantando a sus crias")
    
    def dormir(self):
        print("El mamífero está durmiendo")

# Clase AnimalDomestico
# Contiene el nombre del dueño y el nombre del animal
# Tiene tres métodos para indicar al usuario que el animal está siendo entrenado,
# que se le están poniendo las vacunas y que el animal está comiendo un alimento determinado a pasarle como parámetro
class AnimalDomestico:
    def __init__(self, dueno:str, nombre:str):
        self.dueno = dueno
        self.nombre = nombre
    
    def entrenar(self):
        print(f"El animal {self.nombre} está siendo entrenado por {self.dueno}")
    
    def poner_vacunas(self):
        print(f"Poniendo vacunas a {self.nombre}")
    
    def comer(self, alimento):
        print(f"El animal {self.nombre} está comiendo {alimento}")

# Clase Perro
# Hereda de las clases Mamifero y AnimalDomestico
# Tiene dos métodos para indicar al usuario que el perro está ladrando y que el perro está jugando
class Perro(Mamifero, AnimalDomestico):
    def __init__(self, patas:int, pelaje:str, dueno:str, nombre:str):
        Mamifero.__init__(self, patas, pelaje)
        AnimalDomestico.__init__(self, dueno, nombre)
    
    def ladrar(self):
        print(f"{self.nombre} dice: Guau Guau Guau!!")
    
    def jugar(self):
        print(f"El perro {self.nombre} está jugando")

# Clase Gato
# Hereda de las clases Mamifero y AnimalDomestico
# Tiene dos métodos para indicar al usuario que el gato está maullando y que el gato está cazando
class Gato(Mamifero, AnimalDomestico):
    def __init__(self, patas:int, pelaje:str, dueno:str, nombre:str):
        Mamifero.__init__(self, patas, pelaje)
        AnimalDomestico.__init__(self, dueno, nombre)
    
    def maullar(self):
        print(f"{self.nombre} dice: Miau Miuau Miau")
    
    def cazar(self):
        print(f"El gato {self.nombre} está cazando")

# Se crean dos perros y dos gatos con sus datos y se guardan en una lista de animales
perro1 = Perro(4, "marrón", "Carlos", "Toby")
perro2 = Perro(4, "negro", "Laura", "Rex")
gato1 = Gato(4, "naranja", "Ana", "Garfield")
gato2 = Gato(4, "blanco", "Pedro", "Gato")

animales = [perro1, perro2, gato1, gato2]

# Se recorre la lista para llamar a los métodos de cada animal y mostrar su comportamiento
for animal in animales:
    animal.amamantar()
    animal.dormir()
    animal.entrenar()
    animal.poner_vacunas()
    animal.comer("pienso")
    
    # Se comprueba el tipo de animal para llamar a los métodos específicos de cada uno
    if isinstance(animal, Perro):
        animal.ladrar()
        animal.jugar()
    elif isinstance(animal, Gato):
        animal.maullar()
        animal.cazar()
    
    print("\n")