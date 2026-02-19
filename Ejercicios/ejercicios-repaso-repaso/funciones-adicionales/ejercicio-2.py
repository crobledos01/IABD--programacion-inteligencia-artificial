# Comprueba si un número es narcisista (igual a la suma de sus dígitos elevados a la cantidad de cifras)
def es_narcisista(numero):
    digitos = str(numero)
    potencia = len(digitos)
    # Suma cada dígito elevado a la cantidad de cifras
    suma = sum(int(digito)**potencia for digito in digitos)
    return suma == numero

# Solicita un número al usuario y muestra si es narcisista
numero = int(input("Introduce un número: "))
if es_narcisista(numero):
    print(f"El número {numero} es narcisista")
else:
    print(f"El número {numero} NO es narcisista")