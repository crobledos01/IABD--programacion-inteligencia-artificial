nota = int(input("Introduce la nota: "))
edad = int(input("Introduce la edad: "))
sexo = input("Introduce el sexo (M/F): ")
if nota >= 5 and edad >= 18 and sexo.upper() == "F":
    print("ACEPTADA")
elif nota >= 5 and edad >= 18 and sexo.upper() == "M":
    print("POSIBLE")
else:
    print("NO ACEPTADA")