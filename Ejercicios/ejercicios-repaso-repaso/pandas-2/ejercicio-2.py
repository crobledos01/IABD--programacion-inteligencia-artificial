import seaborn as sns
import numpy as np
import pandas as pd

# Se carga el dataset
titanic = sns.load_dataset("titanic")

# Se carga solo los valores en los que la persona ha sobrevivido y se crea una tabla pivote
tabla = titanic[titanic["survived"] == 1].pivot_table(
    # index (sex) corresponde a las filas, columns (class) a las columnas y values (age) a los valores de la tabla
    # aggfunc se utiliza para calcular la edad máxima, mínima y media
    index="sex",
    columns="class",
    values="age",
    aggfunc=[np.max, np.min, np.mean]
)

# Se redondean los valores hacia arriba utilizando np.ceil
tabla = np.ceil(tabla)
print("TABLA PIVOTE:")
print(tabla)

comprobacion = (
    # Se carga solo los valores en los que la persona ha sobrevivido
    titanic[titanic["survived"] == 1]
        # Se agrupan los supervivientes por sexo y clase y se selecciona la columna edad
        .groupby(["sex", "class"], observed=True)["age"]
        # Se agregan las estadísticas de edad máxima, mínima y media, redondeando hacia arriba
        .agg(
            edad_maxima = lambda x: int(np.ceil(x.max())),
            edad_minima = lambda x: int(np.ceil(x.min())),
            edad_media = lambda x: int(np.ceil(x.mean()))
        )
)

# Se imprime el resultado
print("\nCOMPROBACIÓN:")
print(comprobacion)