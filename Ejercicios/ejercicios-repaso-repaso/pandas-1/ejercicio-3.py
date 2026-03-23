import pandas as pd

# Se recoge el csv y se añade a un dataframe
df = pd.DataFrame(pd.read_csv('house_corregido.csv'))

# Se crea una lista con las columnas indicadas
localizacion = ['street', 'city', 'statezip', 'country']

# Se crea una lista para añadir las columnas que no se encuentren en la lista anterior
caracteristicas = [col for col in df.columns if col not in localizacion]

# Se agrupan en tuplas los grupos según si es parte de la localización o no
tuplas = [(('localizacion', col)
            if col in localizacion
            else ('caracteristicas', col)) 
            for col in df.columns]

# Se crea un multiindex para agrupar por filas independientemente de qué grupo se trate pero indicándolo
# de esta forma, se puede saber qué campo pertenece a localizacion y qué campo pertenece a características
multi_index = pd.MultiIndex.from_tuples(tuplas, names=['grupo', 'columna'])

# Se modifica el DataFrame para que quede dividido en columnas
# separando los cuatro campos dentro de df['localizacion'] y el resto en df['caracteristicas']
df.columns = multi_index

# Se ordena el DataFrame por grupos y filas
df = df.sort_index(axis=1, level=0)

# Se crea un nuevo DataFrame solo con los valores de localizacion y se imprime
df_localizacion = df['localizacion']
print(df_localizacion.head())