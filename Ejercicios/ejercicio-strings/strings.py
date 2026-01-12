cadena = input("Introduce una cadena: ")

while True:
  caracter1 = input("Introduce una vocal: ")
  if len(caracter1)==1 and caracter1 in 'aeiou':
    break
  print("Se debe introducir UNA SOLA VOCAL")

while True:
  caracter2 = input("Introduce otra vocal: ")
  if len(caracter2)==1 and caracter2 in 'aeiou':
    break
  print("Se debe introducir UNA SOLA VOCAL")

cadena = cadena.replace(caracter1.lower(), caracter1.upper()).replace(caracter2.lower(), caracter2.upper())
print(cadena)