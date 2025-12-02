numero = int(input("Introduce un número: "))

print("Factorial recursivo:")
total_r = 1
for i in range(1, numero + 1):
    total_r = total_r * i
    if i == numero:
        print(i, "=", total_r)
    else:
        print(i, end=" * ")

print("Factorial iterativo: ")
total_i = 1
for i in range(1, numero + 1):
    print(i, "*", total_i, "=", i * total_i)
    total_i = total_i * i