def es_armstrong(numero):
    
    cuenta = 0
    for n in numero:
        cuenta = cuenta + int(n) ** len(numero)

    if cuenta == int(numero):
        return True
    else:
        return False

numero = input("Comprueba si un número es Armstrong: ")
if (es_armstrong(numero)):
    print("El número", numero, "es un número Armstrong")
else:
    print("El número", numero, "no es un número Armstrong")