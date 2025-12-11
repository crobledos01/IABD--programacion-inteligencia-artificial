class Estudiante:
    def __init__(self, nombre, edad, nota_media):
        self.nombre = nombre
        self.edad = edad
        self.nota_media = nota_media

def calificar(estudiante):
    if estudiante.nota_media >= 5:
        print("El estudiante", estudiante.nombre, "ha aprobado con una nota media de", estudiante.nota_media)
    else:
        print("El estudiante", estudiante.nombre, "ha suspendido con una nota media de", estudiante.nota_media)

nombre = input("Introduce el nombre del estudiante: ")
edad = int(input("Introduce la edad del estudiante: "))
nota_media = float(input("Introduce la nota media del estudiante: "))

estudiante = Estudiante(nombre, edad, nota_media)

calificar(estudiante)