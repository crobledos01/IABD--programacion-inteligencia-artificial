import pandas as pd
from pathlib import Path

# 1) Carga del dataset como dataframe.
data_path = Path('./data')
columns = ['AirportID', 'Name', 'City', 'Country', 'IATA', 'ICAO', 'Latitude', 'Longitude', 'Altitude', 'Offset', 'DST', 'Tz', 'Type', 'Source']
df = pd.read_csv(data_path / 'airports.csv', header=None, names=columns)

# 2) Muestra las primeras 10 filas del dataframe.
print("EJERCICIO 2:")
print(df.head(10))

# 3) Obtén un resumen estadístico.
print("\n\nEJERCICIO 3:")
print(df.describe(include='all'))

# 4) Para este análisis no vamos a emplear las columnas 'AirportID', 'Latitude', 'Longitude' y 'Altitude', elimínalas del dataframe.
df_limpio = df.drop(columns=['AirportID', 'Latitude', 'Longitude', 'Altitude'])

# 5) Vuelve a obtener un resumen estadístico, ¿de qué forma han cambiado los datos?.
# Se han eliminado las columnas indicadas y se han eliminado del resumen las estadísicas relacionadas a valores numéricos (mean, std, min, 25%, 50%, 75% y max)
print("\n\nEJERCICIO 5:")
print(df_limpio.describe(include='all'))

# 6) Sobre el resumen estadístico anterior parece que en la columna TZ hay un valor raro \N, revisa la proporción de los mismos con value_counts.
print("\n\nEJERCICIO 6:")
print(df['Tz'].value_counts(dropna=False))

# 7) Vuelve a cargar el dataset de modo que se interpreten correctamente los valores nulos (repite el apartado 4, borra las columnas).
df = pd.read_csv(
    data_path / 'airports.csv',
    header=None,
    names=columns,
    na_values='\\N'
)
df = df.drop(columns=['AirportID', 'Latitude', 'Longitude', 'Altitude'])

# 8) Diseña y desarrolla una función para revisar los value_counts de cada columna.
def revision_value_counts(df):
    for col in df.columns:
        print(f'\n--- {col} ---')
        print(df[col].value_counts(dropna=False))

print("\n\nEJERCICIO 8:")
revision_value_counts(df)

# 9) Diseña y desarrolla una función que sobrescriba los valores nulos de las columnas IATA e ICAO por el valor 'DESCONOCIDO'.
# Diseñala para que te permita aceptar cualquier columna y cualquier valor a sobreescribir.
def rellenar_nulos(df, columna, valor):
    df[columna] = df[columna].fillna(valor)
    return df

df = rellenar_nulos(df, 'IATA', 'DESCONOCIDO')
df = rellenar_nulos(df, 'ICAO', 'DESCONOCIDO')

# 10) Implementa una función que te ayude a cambiar el tipo de las variables DST y TZ como categórico.
# Desarrolla tu función para que te permita cambiar cualquier tipo de cualquier columna.
def cambiar_tipo(df, columna, tipo):
    df[columna] = df[columna].astype(tipo)
    return df

df = cambiar_tipo(df, 'DST', 'category')
df = cambiar_tipo(df, 'Tz', 'category')

# 11) Implementa una función que te termina ver en pantalla un resumen estadístico de todas las variables categóricas.
def resumen_categoricas(df):
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    return df[cat_cols].describe()

print("\n\nEJERCICIO 11:")
print(resumen_categoricas(df))

# 12) Diseña y desarrolla una función que te permita agrupar el dataframe por el tipo de aeropuerto, mostrando el conteo de los tipos.
# Tu función debe estar preparada para agrupar por cualquier campo.
def agrupar_conteo(df, columna):
    return df.groupby(columna).size().reset_index(name='conteo')

print("\n\nEJERCICIO 12:")
print(agrupar_conteo(df, 'Type'))

# 13) Selecciona el nombre de las ciudades cuyo tipo de aeropuerto sea "port".
ciudades_port = df.loc[df['Type'] == 'port', 'City'].dropna().unique()

print("\n\nEJERCICIO 13:")
print(ciudades_port)

# 14) Muestra todas las filas de los campos nombre del aeropuerto, nombre del país, nombre de la ciudad y tipo de puerto cuyo país sea Spain.
espana = df.loc[
    df['Country'] == 'Spain',
    ['Name', 'Country', 'City', 'Type']
]

print("\n\nEJERCICIO 14:")
print(espana)

# 15) Muestra el nombre del país, del aeropuerto y tipo que sean pertenecientes de la ciudad de Madrid y Barcelona. ¿Todos los registros son de España?
# No todos los registros son de españa porque hay un aeropuerto en Venezuela en una ciudad que también se llama Barcelona
madrid_barcelona = df.loc[
    df['City'].isin(['Madrid', 'Barcelona']),
    ['Country', 'Name', 'Type', 'City']
]

print("\n\nEJERCICIO 15:")
print(madrid_barcelona)

print(madrid_barcelona['Country'].unique())

# 16) Guarda los resultados anteriores en un csv llamado Madrid_Barcelona en formato csv y excel.
data_path.mkdir(exist_ok=True)
madrid_barcelona.to_csv(data_path / 'Madrid_Barcelona.csv', index=False)