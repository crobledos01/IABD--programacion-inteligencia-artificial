altura = int(input("Introduce la altura de la pirámide: "))
anchura = altura * 2
for i in range(0, altura):
    for j in range(1, (int(anchura / 2) - i)):
        print(end=" ")
    for k in range(1, (i * 2) + 2):
        print(end="*")
    print()