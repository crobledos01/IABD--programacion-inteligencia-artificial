numero = int(input("Introduce un número de dos dígitos: "))
numero_invertido = (numero % 10) * 10 + (numero // 10)
print("El número con los dígitos invertidos es:", numero_invertido)