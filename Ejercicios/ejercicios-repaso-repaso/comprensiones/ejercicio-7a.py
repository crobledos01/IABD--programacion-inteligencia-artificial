# Se crea una lista de números del 1 al 100
numeros = list(range(1, 101))
# Se muestra la lista original por claridad
print(numeros)
resultado = []
# Se recorre cada número y se aplican varios if anidados para las condiciones
for n in numeros:
    # Si es divisible entre 3 y 5 a la vez
    if n % 3 == 0 and n % 5 == 0:
        resultado.append("ÑAM_ÑAM_A_COMER")
    # Si es divisible solo entre 3
    elif n % 3 == 0:
        resultado.append("ÑAM")
    # Si es divisible solo entre 5
    elif n % 5 == 0:
        resultado.append("A_COMER")
    # En cualquier otro caso se añade el número tal cual
    else:
        resultado.append(n)
# Se imprime la lista final con las sustituciones realizadas
print("Lista final: ")
print(resultado)