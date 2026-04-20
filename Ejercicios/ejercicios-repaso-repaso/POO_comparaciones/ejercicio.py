import random

# Clase Objeto
# Contiene el nombre del objeto y su peso
# Al hacer print de un objeto, llama a la función __str__ para mostrar sus datos
class Objeto:
    def __init__(self, nombre_objeto, peso):
        self.nombre_objeto = nombre_objeto
        self.peso = peso

    def __str__(self):
        return f"{self.nombre_objeto}: {self.peso}Kg"

# Clase Persona
# Contiene el nombre, edad, altura y una lista de objetos que posee
class Persona:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.objetos = []

    # Se realiza un bucle con un número del 1 al 5 para crear objetos aleatorios y añadirlos a la lista de objetos de la persona
    def agregar_objetos_aleatorios(self):
        num_objetos = random.randint(1, 5)
        for i in range(num_objetos):
            nombre = f"Objeto {i + 1}"
            peso = random.randint(1, 10)
            self.objetos.append(Objeto(nombre, peso))

    # Se devuelve el objeto con el peso más alto de la lista de objetos de la persona
    def objeto_mas_pesado(self):
        return max(self.objetos, key=lambda obj: obj.peso)

    # Muestra el nombre, edad, altura y la lista de objetos de la persona. Si no tiene objetos
    def __str__(self):
        return f"{self.nombre} ({self.edad} años, {self.altura} cm)"

# Se crea una lista de objetos de personas
personas = [
    Persona("Juan", 70, 180),
    Persona("María", 25, 170),
    Persona("Pedro", 30, 170),
    Persona("Antonio", 30, 200)
]

# Se recorre la lista de personas y se llama a la función que le agrega objetos a cada una
for persona in personas:
    persona.agregar_objetos_aleatorios()

# Se muestra el objeto de cada persona y una lista de sus objetos
print("PERSONAS Y SUS OBJETOS")
for persona in personas:
    print(f"\n{persona}")
    for obj in persona.objetos:
        print(f"  - {obj}")

# Se muestra la persona con el objeto más pesado y el objeto más pesado de esta y la persona con más objetos y el número de objetos que tiene
print("\nPersona con el objeto más pesado:", max(personas, key=lambda p: p.objeto_mas_pesado().peso))
print("Su objeto más pesado es el", max(personas, key=lambda p: p.objeto_mas_pesado().peso).objeto_mas_pesado())
print("\nPersona con más objetos:", max(personas, key=lambda p: len(p.objetos)))
print("Número de objetos de esta:", len(max(personas, key=lambda p: len(p.objetos)).objetos))