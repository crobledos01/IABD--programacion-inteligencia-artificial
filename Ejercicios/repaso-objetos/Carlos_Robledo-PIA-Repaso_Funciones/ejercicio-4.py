#Se crea la clase con las 3 variables
class Estudiante:
    def __init__(self, nombre, edad, nota_media):
        self.nombre = nombre
        self.edad = edad
        self.nota_media = nota_media

#Se crea la función de calificar, se le debe pasar un objeto de la clase estudiante.
#Dentro se comprueba que nota_media dentro de estudiante sea al menos 5 para poner el mensaje de aprobado o suspendido que corresponda
def calificar(estudiante):
    if estudiante.nota_media >= 5:
        print("El estudiante", estudiante.nombre, "ha aprobado con una nota media de", estudiante.nota_media)
    else:
        print("El estudiante", estudiante.nombre, "ha suspendido con una nota media de", estudiante.nota_media)

#Se le piden los datos del estudiante al usuario
nombre = input("Introduce el nombre del estudiante: ")
edad = int(input("Introduce la edad del estudiante: "))
nota_media = float(input("Introduce la nota media del estudiante: "))

#Se crea un estudiante utilizando la clase y se llama a la función para calificarle
estudiante = Estudiante(nombre, edad, nota_media)
calificar(estudiante)