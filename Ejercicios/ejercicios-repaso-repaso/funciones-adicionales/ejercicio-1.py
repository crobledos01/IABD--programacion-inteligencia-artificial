import random

# Genera una lista de 5 tiradas aleatorias de dados con valores entre 1 y 6
def generar_tiradas():
    tiradas = []
    for _ in range(0, 5):
        tiradas.append(random.randint(1, 6))

    return tiradas

# Calcula la puntuación de la lista de dados según las reglas del juego Codicia
def codicia(dados):
    puntuacion = 0
    # Conteo de ocurrencias de cada valor de dado
    conteo = {i: dados.count(i) for i in range(1, 7)}
    # Se suman puntos por tríos y por unos/cincos sueltos
    for num in conteo:
        if conteo[num] >= 3:
            if num == 1:
                puntuacion += 1000
            else:
                puntuacion += num * 100
            conteo[num] -= 3
    
    puntuacion += conteo[1] * 100
    puntuacion += conteo[5] * 50
    
    return puntuacion

# Bucle principal para jugar varias partidas
seguir_jugando = True
while seguir_jugando:
    # Pregunta al usuario si quiere jugar otra partida
    seguir_jugando = (input("¿Jugar partida? Introduce S/N: ") == "S")
    if seguir_jugando:
        tiradas = generar_tiradas()
        print(f"Tus tiradas son: {tiradas}")
        print("Tu puntuación es:", codicia(tiradas))
