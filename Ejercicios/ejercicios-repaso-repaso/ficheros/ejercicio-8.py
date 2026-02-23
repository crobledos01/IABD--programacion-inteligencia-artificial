import csv

# ---------------------------------------------------------
# 1) Leer fichero CSV y ordenar por apellidos
# ---------------------------------------------------------

def leer_calificaciones(ruta: str):
    with open(ruta, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        alumnos = list(lector)
    alumnos.sort(key=lambda a: a["Apellidos"])
    return alumnos

# ---------------------------------------------------------
# 2) Aplicar convocatoria ordinaria a cada alumno
# ---------------------------------------------------------

def aplicar_ordinarias(alumno):
    campos = ["Parcial1", "Parcial2", "Practicas"]
    campos_ord = ["Ordinario1", "Ordinario2", "OrdinarioPracticas"]

    notas = {}

    for base, ordn in zip(campos, campos_ord):
        nota_str = alumno.get(base, "").strip().replace(",", ".")
        ord_str = alumno.get(ordn, "").strip().replace(",", ".")

        nota = float(nota_str) if nota_str else 0.0
        nota_ord = float(ord_str) if ord_str else None

        if nota < 4 and nota_ord is not None and nota_ord > nota:
            notas[base] = nota_ord
        else:
            notas[base] = nota

    return notas

# ---------------------------------------------------------
# 3) Añadir la nota final a cada alumno
# ---------------------------------------------------------

def anadir_nota_final(alumnos):
    for alumno in alumnos:
        notas = aplicar_ordinarias(alumno)
        n1 = notas["Parcial1"]
        n2 = notas["Parcial2"]
        np = notas["Practicas"]

        nota_final = 0.3 * n1 + 0.3 * n2 + 0.4 * np
        alumno["NotaFinal"] = round(nota_final, 2)

# ---------------------------------------------------------
# 4) Separar aprobados y suspensos
# ---------------------------------------------------------

def separar_aprobados_suspensos(alumnos):
    aprobados = []
    suspensos = []

    for a in alumnos:
        asist_str = a["Asistencia"].strip().replace("%", "")
        asistencia = float(asist_str.replace(",", ".")) if asist_str else 0.0

        notas = aplicar_ordinarias(a)
        n1 = notas["Parcial1"]
        n2 = notas["Parcial2"]
        np = notas["Practicas"]
        nf = float(a["NotaFinal"])

        if (
            asistencia >= 75
            and n1 >= 4
            and n2 >= 4
            and np >= 4
            and nf >= 5
        ):
            aprobados.append(a)
        else:
            suspensos.append(a)

    return aprobados, suspensos

# ---------------------------------------------------------
# 5) Ejemplo de uso completo
# ---------------------------------------------------------

ruta_csv = "calificaciones.csv"

print("---------------------------\nAlumnos ordenados por apellidos:\n")
alumnos = leer_calificaciones(ruta_csv)
for alumno in alumnos:
    print(f"{alumno['Apellidos']}, {alumno['Nombre']}.\t"
          f"{'\t' if (len(alumno['Apellidos']) + len(alumno['Nombre'])) < 21 else ''}"
          f"Asistencia: {alumno["Asistencia"]}.\t"
          f"Parcial 1: {alumno["Parcial1"]}, parcial 2: {alumno["Parcial2"]}")


print("\n---------------------------\nNotas finales:\n")
anadir_nota_final(alumnos)
for alumno in alumnos:
    print(f"{alumno['Apellidos']}, {alumno['Nombre']}: {alumno['NotaFinal']}")


print("\n---------------------------\nAlumnos aprobados y suspendidos:\n")
aprobados, suspensos = separar_aprobados_suspensos(alumnos)
print("Aprobados:")
for a in aprobados:
    print(a["Apellidos"], a["Nombre"], a["NotaFinal"])

print("\nSuspendidos:")
for a in suspensos:
    print(a["Apellidos"], a["Nombre"], a["NotaFinal"])
