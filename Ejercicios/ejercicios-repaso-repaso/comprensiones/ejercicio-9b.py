# Se define un array con diccionarios para cada alumno y sus notas
alumnos = [{"Pedro":[5,7,9]},{"Sergio":[3,3,3]},{"Ibtihal":[5,5,5]},{"Angel":[7,7,9]},{"Fede":[5,5,7]}, {"Mik": [7,5,10]}]
# Se crea una lista utilizando una comprensión que incluye:
## Un diccionario que contiene el nombre y la nota media del alumno
## Un bucle que recorre cada alumno
## Otro bucle que obtiene el nombre y las notas del alumno
## Una condición que filtra por longitud del nombre y nota media
resultado = [
    {nombre: round(sum(notas)/len(notas), 1)}
    for alumno in alumnos
    for nombre, notas in alumno.items()
    if len(nombre) >= 4 and (sum(notas)/len(notas)) > 6
]
# Se imprime el resultado
print("Los alumnos con nombre de al menos 4 letras y nota media superior a 6 son: ")
print(resultado)