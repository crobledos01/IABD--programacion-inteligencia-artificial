# Importo el sys para que salga del programa si los dos números son iguales
import sys

# Imprime los divisores de cada número de forma consecutiva y añadiendo + entre cada uno
def imprimirDivisores(divisores):
    for index, num in enumerate(divisores):
        if index != 0:
            print(" + ", end="")
        print(num, end="")

# Calcula los divisores haciendo un bucle desde 1 hasta la mitad del número
# Añade a un array los que den 0 en el resto al dividir y al acabar devuelve los divisores
def calcDivisores(numero):
    divisores = []
    i = 1
    while i <= numero / 2:
        if numero % i == 0:
            divisores.append(i)
        i += 1
    return divisores

# Se piden los números
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

# Se llama a la función que calcula los divisores
divisores1 = calcDivisores(numero1)
divisores2 = calcDivisores(numero2)

# Si los dos números son iguales para el programa
if numero1 == numero2:
    print("Los números iguales no pueden ser amigos")
    sys.exit(0)

# Imprime cada número, dice sus divisores llamando a la función y los suma
print(f"Divisores del número {numero1}: ", end="")
imprimirDivisores(divisores1)
print(f" = {sum(divisores1)}")
print(f"Divisores del número {numero2}: ", end="")
imprimirDivisores(divisores2)
print(f" = {sum(divisores2)}")

# Si la suma de los divisores del primer número es igual al segundo número y viceversa, los números son amigos
if sum(divisores1) == numero2 and sum(divisores2) == numero1:
    print(f"Los números {numero1} y {numero2} son números amigos")
else:
    print(f"Los números {numero1} y {numero2} NO son números amigos")