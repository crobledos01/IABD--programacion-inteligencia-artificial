# Se crea el array con los porcentajes
porcentajes = [12, "23.5", None, 98.125, None, "73", 25.1, "55.238", 87, None, 21.02]
# Se crea un array con comprensión para formatear los porcentajes. De arriba a abajo:
## Si no es un string, como el if final tiene prioridad, solo pueden quedar los tipos int y float. Por tanto, se redondea directamente ya que ambos lo permiten
## En caso contrario (es decir, si es un string), se pasa a float y se redondea con dos decimales
## Se realiza un bucle para pasar por cada uno de los porcentajes
## Este if sirve para que no tenga en cuenta los None
porcentajes_formateados = [
    round(p, 2) if not isinstance(p, str)
    else round(float(p), 2)
    for p in porcentajes
    if p is not None
]
# Se imprime el resultado
print(porcentajes_formateados)