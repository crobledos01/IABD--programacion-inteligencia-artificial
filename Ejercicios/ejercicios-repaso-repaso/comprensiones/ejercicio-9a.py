# Se define un array con diccionarios para cada alumno y sus notas y el array resultado
alumnos = [{"Pedro":[5,7,9]},{"Sergio":[3,3,3]},{"Ibtihal":[5,5,5]},{"Angel":[7,7,9]},{"Fede":[5,5,7]}, {"Mik": [7,5,10]}]
resultado = []
# Se recorren los alumnos y, dentro de cada uno, su nombre y sus notas
for alumno in alumnos:
    for nombre, notas in alumno.items():
        # Se calcula la nota media
        nota_media = round(sum(notas)/len(notas), 1)
        # Si cumple las condiciones se añade al resultado
        if len(nombre) >= 4  and nota_media > 6:
            resultado.append({nombre: nota_media})
# Se imprime el resultado
print("Los alumnos con nombre de al menos 4 letras y nota media superior a 6 son: ")
print(resultado)