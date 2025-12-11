import math

#Imprime los números.
#Se realiza un if != 0 que añade una coma antes de cada número excepto antes del primer valor
def imprimir(numeros):
    for index, n in enumerate(numeros):
        if index != 0:
            print(end=", ")
        print(n, end="")

#Se realiza la criba de Eratóstenes.
#Para ello, primero se calcula la raíz cuadrada del número, porque todos los múltiplos de un número mayor que su raíz ya habrán
#       sido eliminados por los números menores, así que no se encontrarán nuevos factores. Se hace un redondeo al alza para dar un número entero
#Después, se hace un bucle para añadir todos los candidatos desde el dos hasta el indicado
#Por último, se hace un nuevo bucle desde el número 2 hasta el límite marcado por la raíz. Dentro de este bucle, se hace otro que recorre
#       desde el doble del número del primer bucle (su primer múltiplo, evitando que se borren los primos) hasta el número introducido.
#       Este nuevo bucle no suma de uno en uno, sino que por cada vez que se recorre se suma el propio número para eliminar todos los múltiplos de este
#Los números que no han sido eliminados son los números primos, que se envían para imprimirlos por consola
def criba(n):
    limite = math.ceil(n ** 0.5)
    numeros = []
    for i in range(2, n + 1):
        numeros.append(i)

    for i in range(2, limite):
        for j in range(i + i, n + 1, i):
            if j in numeros:
                numeros.remove(j)
    
    imprimir(numeros)

#Se pide el número por consola y se llama a la función
n = int(input("Introduce el número límite: "))
criba(n)