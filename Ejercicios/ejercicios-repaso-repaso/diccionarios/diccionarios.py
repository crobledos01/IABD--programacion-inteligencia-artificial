# Se pega el verso y se crea el diccionario con las 5 vocales en minúsculas
cadena = "En un lugar de la Mancha2, de cuyo nombre no quiero acordarme3, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor4. Una olla de algo más vaca que carnero, salpicón las más noches5, duelos y quebrantos los sábados6, lantejas los viernes7, algún palomino de añadidura los domingos8, consumían las tres partes de su hacienda9. El resto della concluían sayo de velarte10, calzas de velludo para las fiestas, con sus pantuflos de lo mesmo11, y los días de entresemana se honraba con su vellorí de lo más fino12. Tenía en su casa una ama que pasaba de los cuarenta y una sobrina que no llegaba a los veinte, y un mozo de campo y plaza que así ensillaba el rocín como tomaba la podadera13. Frisaba la edad de nuestro hidalgo con los cincuenta años14. Era de complexión recia, seco de carnes, enjuto de rostro15, gran madrugador y amigo de la caza."
vocales = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0,
}
# Se recorre la cadena caracter a caracter pasando cada letra a minúscula
for c in cadena.lower():
    # Si el caracter es una vocal, se suma uno en el diccionario en la posición correspondiente
    if c in vocales:
        vocales[c] = vocales[c] + 1
# Al acabar, se imprime el calendario
print("Mostramos el número de apariciones de cada vocal en el fragmento del Quijote: ")
print(vocales)