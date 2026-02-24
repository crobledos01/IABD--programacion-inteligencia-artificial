import csv

# Esta función lee el archivo CSV y devuelve una lista de diccionarios de alumnos y sus notas, ordenados por apellidos.
def leer_calificaciones(ruta: str):
    with open(ruta, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        alumnos = list(lector)
    alumnos.sort(key=lambda a: a["Apellidos"])
    return alumnos

# Esta función convierte una nota a formato decimal, teniendo en cuenta que si está vacía la nota es 0 y que si la nota es mayor que 10, se asume que está en formato de 0 a 100 y se divide entre 10.
def convertir_nota(nota):
    if nota.strip() == "":
        return 0.0
    else:
        nota = float(nota)
        if nota > 10:
            nota = nota / 10
        return(nota)

# Esta función calcula la nota final del alumno
# Para ello, utiliza la fórmula: 0.3 * parcial1 + 0.3 * parcial2 + 0.4 * practicas
# Si la nota final es menor que 5, se calcula de nuevo siguiendo el mismo criterio con las notas del ordinario
def anadir_nota_final(alumnos):
    for alumno in alumnos:

        nota_final = 0.3 * convertir_nota(alumno["Parcial1"]) + 0.3 * convertir_nota(alumno["Parcial2"]) + 0.4 * convertir_nota(alumno["Practicas"])
        if nota_final < 5:
            nota_final = 0.3 * convertir_nota(alumno["Ordinario1"]) + 0.3 * convertir_nota(alumno["Ordinario2"]) + 0.4 * convertir_nota(alumno["OrdinarioPracticas"])
        alumno["NotaFinal"] = round(nota_final, 2)

# Esta función crea dos listas, una con los alumnos aprobados y otra con los alumnos suspendidos, y añade cada alumno a la lista correspondiente
def separar_aprobados_suspensos(alumnos):
    aprobados = []
    suspensos = []

    for alumno in alumnos:
        if alumno["NotaFinal"] >= 5:
            aprobados.append(alumno)
        else:
            suspensos.append(alumno)

    return aprobados, suspensos

# Nombre del archivo CSV. Para que funcione, el archivo y el script deben estar en la misma carpeta que la terminal en la que se va a correr el código
ruta_csv = "calificaciones.csv"


print("---------------------------\nAlumnos ordenados por apellidos:\n")
# Para esto, se llama a leer_calificaciones, que devuelve la lista de diccionarios de alumnos ordenadas por apellidos
# Se recorre la lista de alumnos y se imprime toda su información
alumnos = leer_calificaciones(ruta_csv)
for alumno in alumnos:
    print(f"{alumno['Apellidos']}, {alumno['Nombre']}.\t"
          # Esta línea sirve para solo para añadir una segunda tabulación a los nombres cortos para que quedan alineados en consola
          f"{'\t' if (len(alumno['Apellidos']) + len(alumno['Nombre'])) < 21 else ''}"
          f"Asistencia: {alumno["Asistencia"]}.\t"
          f"Parcial 1: {alumno["Parcial1"]}, parcial 2: {alumno["Parcial2"]}")


print("\n---------------------------\nNotas finales:\n")
# Para ello, se llama a anadir_nota_final, que añade la nota a cada alumno en el diccionario, y se recorre la lista de alumnos
anadir_nota_final(alumnos)
for alumno in alumnos:
    print(f"{alumno['Apellidos']}, {alumno['Nombre']}: {alumno['NotaFinal']}")


print("\n---------------------------\nAlumnos aprobados y suspendidos:\n")
# Para esto, se crean dos listas y se llama a separar_aprobados_suspensos, y se recorren ambas listas para mostrar cada uno
aprobados, suspensos = separar_aprobados_suspensos(alumnos)
print("Aprobados:")
for a in aprobados:
    print(a["Apellidos"], a["Nombre"], a["NotaFinal"])

print("\nSuspendidos:")
for a in suspensos:
    print(a["Apellidos"], a["Nombre"], a["NotaFinal"])
