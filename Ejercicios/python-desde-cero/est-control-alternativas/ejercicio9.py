numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))
if numero1 >= numero2 and numero1 >= numero3 and numero2 >= numero3:
    print("El orden de los números es: ", numero1, ", ", numero2, ", ", numero3)
elif numero1 >= numero2 and numero1 >= numero3 and numero3 >= numero2:
    print("El orden de los números es: ", numero1, ", ", numero3, ", ", numero2)
elif numero2 >= numero1 and numero2 >= numero3 and numero1 >= numero3:
    print("El orden de los números es: ", numero2, ", ", numero1, ", ", numero3)
elif numero2 >= numero1 and numero2 >= numero3 and numero3 >= numero1:
    print("El orden de los números es: ", numero2, ", ", numero3, ", ", numero1)
elif numero3 >= numero1 and numero3 >= numero2 and numero1 >= numero2:
    print("El orden de los números es: ", numero3, ", ", numero1, ", ", numero2)        
else:
    print("El orden de los números es: ", numero3, ", ", numero2, ", ", numero1)