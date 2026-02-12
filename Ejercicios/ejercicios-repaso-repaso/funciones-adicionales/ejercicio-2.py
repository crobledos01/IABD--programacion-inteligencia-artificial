def es_narcisista(numero):
    digitos = str(numero)
    potencia = len(digitos)
    suma = sum(int(digito)**potencia for digito in digitos)
    return suma == numero

numero = int(input("Introduce un número: "))
if es_narcisista(numero):
    print(f"El número {numero} es narcisista")
else:
    print(f"El número {numero} NO es narcisista")