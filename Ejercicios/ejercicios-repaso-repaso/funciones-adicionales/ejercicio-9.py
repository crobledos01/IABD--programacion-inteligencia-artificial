import random

# Genera una lista de 3 jugadas aleatorias para la máquina (R, P, S)
def obtener_jugadas():
    jugadas = []
    for _ in range(0, 3):
        jugadas.append(random.choice(["R", "S", "P"]))
    return jugadas

# Calcula el resultado de la partida entre dos listas de jugadas
def juego(jugadas1, jugadas2):
    puntos1 = 0
    puntos2 = 0
    # Diccionario de posibilidades: 1 gana jugador 1, 2 gana jugador 2
    posibilidades = {
        ("R", "S"): 1,
        ("S", "P"): 1,
        ("P", "R"): 1,
        ("S", "R"): 2,
        ("P", "S"): 2,
        ("R", "P"): 2
    }
    # Compara cada jugada
    for index, _ in enumerate(jugadas1):
        if jugadas1[index] != jugadas2[index]:
            ganador = posibilidades.get((jugadas1[index], jugadas2[index]))
            if ganador == 1:
                puntos1 += 1
            elif ganador == 2:
                puntos2 += 1
    # Muestra el resultado final
    if puntos1 > puntos2:
        print("El ganador es el jugador 1")
    elif puntos2 > puntos1:
        print("El ganador es el jugador 2")
    else:
        print("El juego ha quedado empate")

# Solicita varias jugadas al usuario y juega contra la máquina
jugadas1 = []
jugadas2 = obtener_jugadas()
jugadas1.append(input("Introduce tu primera jugada (P, R o S): "))
print(f"La primera jugada del rival es: {jugadas2[0]}")
jugadas1.append(input("Introduce tu segunda jugada: "))
print(f"La primera jugada del rival es: {jugadas2[1]}")
jugadas1.append(input("Introduce tu tercera jugada: "))
print(f"La primera jugada del rival es: {jugadas2[2]}")
juego(jugadas1, jugadas2)
