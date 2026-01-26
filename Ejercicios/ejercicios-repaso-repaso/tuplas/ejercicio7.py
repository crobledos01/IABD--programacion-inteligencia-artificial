# Se genera una tupla para los divisores y otra para los dividendos y una lista que contendrá ambas, el signo del resto y el propio resto
tupla_divisores = (10, 4, 5, 6)
tupla_dividendos = (5, 6, 7, 5)
lista_operaciones = []
# Se realiza un for con la agrupación de las dos tuplas para realizar las operaciones
# Dentro, se añaden a la lista anterior los valores, el símbolo y el resto de la división
for divisor, dividendo in zip(tupla_divisores, tupla_dividendos):
    lista_operaciones.append((divisor, dividendo, '%', dividendo % divisor))
# Se transforma la lista a tupla y se imprime
tupla_operaciones = tuple(lista_operaciones)
print(tupla_operaciones)