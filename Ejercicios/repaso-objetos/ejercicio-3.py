class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

def saludar(persona):
    print("Hola, soy", persona.nombre)


persona = Persona("Carlos")

saludar(persona)