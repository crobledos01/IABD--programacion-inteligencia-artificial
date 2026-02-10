# Se crea la matriz de números
matriz = [[[1, 2], [3,4]], [[5]]]
# Se crea el array resultado utilizando comprensión. Para ello:
## "numero" añade al array cada número
## El primer for divide la matriz en dos grupos, que pasarían a ser: [[1, 2], [3,4]] por un lado y [[5]] por otro
## El segundo for divide cada uno de los dos grupos anteriores, de manera que el primer grupo pasaría a dividirse en [1, 2] y [3, 4], mientras que [[5]] pierde un corchete:[5]
## El tercer array divide cada uno de los números ya por separado
desempaquetado = [
    numero
    for grupo in matriz
    for numeros in grupo
    for numero in numeros
]
# Se crea la matriz de nombres
grupo_nombres = [["alIcia", 'aDam', "AbiliO"], ['Dylan', 'DiANa']]
# Se crea el array resultado utilizando comprensión. Para ello:
## Se añade cada nombre al array utilizando .capitalize() para dejar solo la primera letra en mayúscula
## El primer for divide la matriz en dos arrays, quedando ["alIcia", 'aDam', "AbiliO"] por un lado y ['Dylan', 'DiANa'] por otro
## El segundo divide cada uno de los nombres por separado
capitalizados = [
    nombre.capitalize()
    for nombres in grupo_nombres
    for nombre in nombres
]
# Se crea el string con el abecedario con algunas letras en mayúscula y otras en minúscula
letras = "ABcdefghIjKLmnÑOpQrStUvWXYZ"
# Se crea un array para guardar solo las letras que estén en mayúscula. Para ello:
## "letra" añade la letra si cumple la condición final
## El bucle recorre el string dejando cada letra por separado
## Solo cuenta la letra si se cumple que .isupper() devuelve true. Es decir, si la letra está en mayúscula
mayus = [
    letra
    for letra in letras
    if letra.isupper()
]
# Se imprime el resultado de las operaciones anteriores
print(desempaquetado)
print(capitalizados)
print(mayus)