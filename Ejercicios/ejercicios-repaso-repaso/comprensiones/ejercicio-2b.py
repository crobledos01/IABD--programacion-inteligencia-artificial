# Se pide la frase al usuario y se divide por palabras
frase = input("Introduce una frase: ")
palabras = frase.split()
# Para dar el resultado final, se utiliza la compresión que se compone de tres partes
## El bucle final que sirve para leer palabra por palabra
## palabra.upper() se realiza si la primera condición (a se encuentra en la palabra) se cumple para poner todo el texto en mayúsculas
## En caso de que no se cumpla la condición, el else indica que se debe realizar palabra.title() para poner en mayúscula solo la primera letra
resultado = [palabra.upper() if("a" in palabra) else palabra.title() for palabra in palabras]
# Se imprime el resultado
print("La frase final es: ")
print(" ".join(resultado))