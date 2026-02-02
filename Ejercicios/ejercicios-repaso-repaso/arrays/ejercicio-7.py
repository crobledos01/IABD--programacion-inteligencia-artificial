# Se importa el módulo array
from array import array
# Se crea un array
lista = array('i', [1, 5, 3, 7, 1, 9, 3])
# Se crea un nuevo array utilizando set del array original como contenido, ya que set elimina los duplicados y deja una lista de los números distintos
lista_sin_duplicados = array('i', set(lista))
# Si ambas listas tienen la misma longitud es que no hay repetidos, por tanto se imprime Falso
if (len(lista) == len(lista_sin_duplicados)):
    print("Falso")
# Si tienen distinta longitud es porque al menos un número duplicado ha desaparecido en la lista que se basa en set y se imprime Verdadero
else:
    print("Verdadero")