import random as random
palabras = ["orangutan", "camello", "pelicula", "tragaperras", "almacen", "iracundo", "participante", "colegio", "tortilla", "mosquitera"]
palabra = palabras[random.randint(0, 9)]
letras = []
ganador = False
for i in range(10):
  print(f"Intento {i + 1}")
  letra = input("Di una letra: ")
  letras.append(letra)
  for c in palabra:
    if c in letras:
      print(c, end="")
    else:
      print("*", end="")
  intentar = input("¿Quieres resolver? S/N: ")
  if intentar.upper() == "S":
    intento = input("Escribe la palabra: ")
    if intento.lower() == palabra.lower():
      ganador = True
      print("ENHORABUENA, MAESTRO. La palabra era: " + palabra)
      break
    else:
      print(f"La palabra {intento} es incorrecta")

if ganador == False:
  print("Te has quedado sin intentos. La palabra era: " + palabra)