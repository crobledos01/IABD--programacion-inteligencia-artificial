import pandas as pd

# Se recoge el csv y se añade a un dataframe
df = pd.DataFrame(pd.read_csv('house_corregido.csv'))

# Se recoge el valor correspondiente al precio en la fila número 256 y se imprime
precio_256 = df.loc[256, 'price']
print(f"Precio de la casa en la fila 256: {precio_256}\n")

# Mismo que lo anterior, pero con habitaciónes y filas del 215 al 223
habs_215_222 = df.loc[215:223, 'bedrooms']
print(f"Número de habitaciones de las filas 215 a 223 es:\n{habs_215_222}\n")

# Utilizando la función sample, se recoge una muestra equivalente al 15%
df_aleatorio = df.sample(frac=0.15)
# Se imprime la longitud de esta muestra con respecto al total
print(f"El DataFrame aleatorio tiene {len(df_aleatorio)} filas de un total de {len(df)}\n")

# Se filtra utilizando la función isin que recoge las casas con 3 o 4 habitación y con un precio menor a 300000
df_filtrado = [(df_aleatorio['bedrooms'].isin([3,4])) & (df_aleatorio['price'] < 300000)]
# Se imprime la longitud para comprobar cuantos valores ha sacado
print(f"Registros con 3 o 4 habitaciones y precio menor a 300.000€: {len(df_filtrado)}")