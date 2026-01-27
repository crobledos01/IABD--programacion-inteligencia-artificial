# Datos de los usuarios
usuarios = {
    1: (25, 3000),
    2: (None, 4500),  
    3: (22, None),    
    4: (30, 3800),
    5: (None, None),  
    6: (27, 5000),
}
# Se crean variables para la edad y el ingreso con el valor más alto
edad_max = 0
ingreso_max = 0
# Utilizando un bucle, se recoge la edad y el ingreso de cada posición en el diccionario
for edad, ingreso in usuarios.values():
    # Si la edad no es nula y es más alta que la edad máxima registrada hasta el momento, se sustituye en la variable
    if edad is not None and edad > edad_max:
        edad_max = edad
    # Si el ingreso no es nulo y es más alto que el ingreso máximo registrado hasta el momento, se sustituye en la variable
    if ingreso is not None and ingreso > ingreso_max:
        ingreso_max = ingreso
# Se crea una lista para los valores normalizados
usuarios_norm = []
# Se recorre de nuevo el diccionario
for edad, ingreso in usuarios.values():
    # Si la edad no es nula, se normaliza dividiéndola entre el valor máxima y redondeando con dos decimales. Si es nula, se mantiene como nula
    if edad is not None:
        edad_norm = round((edad / edad_max), 2)
    else:
        edad_norm = None
    # Si el ingreso no es nulo, se normaliza dividiéndolo entre el valor máximo y redondeando con dos decimales. Si es nulo, se mantiene como nulo
    if ingreso is not None:
        ingreso_norm = round((ingreso / ingreso_max), 2)
    else:
        ingreso_norm = None
    # Se añaden la edad y el ingreso normalizados a la lista de usuarios
    usuarios_norm.append((edad_norm, ingreso_norm))
# Se imprimen todos los usuarios
print("La lista de usuarios e ingresos normalizada es: ")
print(usuarios_norm)
