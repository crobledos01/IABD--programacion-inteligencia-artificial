import pandas as pd

# Se recoge el csv y se añade a un dataframe
df = pd.DataFrame(pd.read_csv('house_corregido.csv'))

# Utilizando la función de pandas to_datetime, se actualiza el valor date transformándolo a fecha
df['date'] = pd.to_datetime(df['date'])

# Se añaden las columnas día, mes y año recurriendo a la función .dt, que recoge el tiempo dividido en los campos necesarios
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

# Se imprimen las nuevas columnas junto a la de date para comprobar
print("Nuevas columnas año, mes y día junto a la fecha original:")
print(df[['date', 'year', 'month', 'day']].head(5))

# Se crea una lista utilizando la función groupby para unir los precios por mes y utilizando mean para obtener la media
print("\nPrecio agrupado por mes:")
df_precio_por_mes = df.groupby('month')['price'].mean()
print(df_precio_por_mes)

# Utilizando la función Timedelta que permite sumar días, meses o años a una fecha, se crea la nueva columna date2
df['date2'] = df['date'] + pd.Timedelta(days=20)
print("\nComparativa de fechas:")
print(df[['date', 'date2']].head(5))