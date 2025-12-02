def esPrimo(numero):
    for i in range (2, numero):
        if numero % i == 0:
            return False
        
    return True

numero = int(input("Introduce un número: "))
primo = esPrimo(numero)
if primo:
    print("El número", numero, "es primo")
else:
    print("El número", numero, "no es primo")