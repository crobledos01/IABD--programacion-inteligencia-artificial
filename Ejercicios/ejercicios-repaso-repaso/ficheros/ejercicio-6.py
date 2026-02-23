import os

RUTA = "contador.txt"

def leer_contador():
    if not os.path.exists(RUTA):
        return 0
    try:
        with open(RUTA, "r", encoding="utf-8") as f:
            contenido = f.read().rstrip()
            if not contenido:
                return 0
            return int(contenido)
    except (ValueError, OSError):
        print("Error: fichero corrupto.")
        return 0

def escribir_contador(valor):
    with open(RUTA, "w", encoding="utf-8") as f:
        f.write(str(valor))

contador = leer_contador()

accion = int(input("¿Qué quieres hacer? (1: incrementar, 2: decrementar, otro: leer valor): "))
match accion:
    case 1:
        contador += 1
    case 2:
        contador -= 1
    case _:
        pass

print(contador)
escribir_contador(contador)