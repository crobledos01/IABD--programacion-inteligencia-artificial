import pandas as pd

# Se recoge el csv y se añade a un dataframe
df = pd.DataFrame(pd.read_csv('house_corregido.csv'))

# Si en el DataFrame hay filas con 8 habitaciones se imprime que existe, si no se imprime que no
if (df['bedrooms'] == 8).any():
    print("Hay al menos una casa con 8 habitaciones.\n")
else:
    print("No hay ninguna casa con 8 habitaciones.\n")

# Se utiliza .min y .max sobre el campo habitaciones para obtener su mínimo y máximo y se imprime el resultado
minimo =  df['bedrooms'].min() 
maximo = df['bedrooms'].max()
print(f"Mínimo habitaciones: {minimo}, Máximo: {maximo}\n")

# Se añade la nueva columna basándose en el precio total dividido entre las plantas totales y se imprime una muestra
df['precio_por_planta'] = df['price'] / df['floors']
print(df[['price', 'floors', 'precio_por_planta']].head())