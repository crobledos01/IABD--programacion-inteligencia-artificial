parcial1 = float(input("Introduce la nota del primer parcial: "))
parcial2 = float(input("Introduce la nota del segundo parcial: "))
parcial3 = float(input("Introduce la nota del tercer parcial: "))
media = (parcial1 + parcial2 + parcial3) / 3
examen = float(input("Introduce la nota del examen final: "))
trabajo = float(input("Introduce la nota del trabajo final: "))
nota_final = (media * 0.55) + (examen * 0.3) + (trabajo * 0.15)
print("La nota final del alumno es:", nota_final)