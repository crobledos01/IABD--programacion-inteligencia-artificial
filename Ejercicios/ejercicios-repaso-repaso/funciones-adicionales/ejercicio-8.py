import random

# Genera una pista aleatoria de obstáculos con una cantidad aleatoria de pasos ("_" para correr, "|" para saltar)
def obtener_pista():
    pasos = []
    for _ in range(0, random.randint(5, 10)):
        pasos.append(random.choice(["|", "_"]))
    resultado = ""
    for p in pasos:
        resultado = resultado + p
    return resultado

# Comprueba si las acciones del usuario coinciden con la pista
def comprobar_carrera(pista, acciones):
    resultado = ""
    
    for index, paso in enumerate(pista):
        # Correcto correr
        if paso == "_" and acciones[index] == "C":
            resultado = resultado + paso
        # Correcto saltar
        if paso == "|" and acciones[index] == "S":
            resultado = resultado + paso
        # Incorrecto correr
        if paso == "_" and acciones[index] == "S":
            resultado = resultado + "x"
        # Incorrecto saltar
        if paso == "|" and acciones[index] == "C":
            resultado = resultado + "/"
    # Muestra si la carrera fue superada o no
    if resultado == pista:
        print("La carrera se ha completado correctamente")
    else:
        print(f"Carrera no superada, el recorrido es: {resultado}")

# Genera la pista y solicita las acciones al usuario
pista = obtener_pista()
acciones = input(f"La pista es: {pista}, introduce S para saltar o C para correr: ")
comprobar_carrera(pista, acciones)