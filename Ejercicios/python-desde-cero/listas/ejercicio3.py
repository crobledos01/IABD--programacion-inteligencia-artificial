lista = []

for index in range(5):
    numero = int(input("Introduce la nota: "))
    if(numero < 0 or numero > 10):
        while numero < 0 or numero > 10:
            numero = int(input("La nota debe estar entre 0 y 10. Introdúcela de nuevo: "))
    lista.append(numero)

print("Las notas introducidas son:", end=" ")
for nota in lista:
    print(nota, end=". ")

print("\nEl nota media es:", sum(lista) / len(lista))
print("La nota más alta es:", max(lista), "y la nota más baja es:", min(lista))