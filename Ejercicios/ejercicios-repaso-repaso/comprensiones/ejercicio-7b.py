# Se crea la lista de números del 1 al 100
numeros = list(range(1, 101))
# Se imprime la lista original
print(numeros)
# Comprensión de listas que aplica varios if anidados para las condiciones
resultado = [
    "ÑAM_ÑAM_A_COMER" if n % 3 == 0 and n % 5 == 0
    else "ÑAM" if n % 3 == 0
    else "A_COMER" if n % 5 == 0
    else n
    for n in numeros
]
# Se imprime la lista resultante con las sustituciones
print("Lista final: ")
print(resultado)