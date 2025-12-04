def invertir_lista(lista):
    lista_inversa = []
    for index, valor in enumerate(lista):
        lista_inversa.append(lista[len(lista) - index - 1])
    
    return lista_inversa

texto_lista = input("Introduce los valores de la lista separados por comas: ")
lista = texto_lista.split(",")

lista_inversa = invertir_lista(lista)

print(lista_inversa)