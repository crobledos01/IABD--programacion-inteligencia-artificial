def esPar(numero):
    if numero % 2 == 0:
        return True
    else:        
        return False

numero = int(input("Introduce un número: "))
par = esPar(numero)
if par:
    print("El número", numero, "es par")
else:
    print("El número", numero, "es impar")