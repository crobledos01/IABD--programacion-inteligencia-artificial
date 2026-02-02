# Se pide la frase al usuario y se crea un array para introducir el resultado
frase = input("Introduce una frase: ")
resultado = []
# Se recorren las palabras en un bucle utilizando split para separar las palabras en la frase
for palabra in frase.split():
    # Si la palabra contiene la letra a, se pone la palabra en mayúsculas
    if "a" in palabra:
        resultado.append(palabra.upper())
    # En caso contrario, se utiliza el formato título para poner solo la primera letra en mayúscula
    else:
        resultado.append(palabra.title())
# Se imprime el resultado final
print("La frase final es: ")
print(" ".join(resultado))