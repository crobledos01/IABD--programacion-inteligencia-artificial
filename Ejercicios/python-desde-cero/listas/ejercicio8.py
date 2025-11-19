nombres = []
edades = []

while True:
    nombre = input("Introduce el nombre del alumno: ")
    if nombre == '*':
        break
    edad = int(input("Añade la edad: "))
    nombres.append(nombre)
    edades.append(edad)

print("Alumnos mayores de edad: ")
for i in range(len(nombres)):
    if edades[i] >= 18:
        print(nombres[i], end=". ")

edades_ordenadas = sorted(edades, reverse=True)

print("\nLos tres alumnos más mayores son: ")
for i in range(0, 3):
    for j in range(len(edades)):
        if edades_ordenadas[i] == edades[j]:
            print(nombres[j], "(", edades[j], ")", end= ".")