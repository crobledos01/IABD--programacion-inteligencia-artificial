nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (M/F): ")
letras_am = "abcdefghijklm"
if sexo == "F":
  if nombre[0].lower() in letras_am:
    print("Perteneces al grupo A")
  else:
    print("Perteneces al grupo B")
elif sexo == "M":
  if nombre[0].lower() not in letras_am:
    print("Perteneces al grupo A")
  else:
    print("Perteneces al grupo B")
else:
  print("El sexo no es válido")