import sqlite3

# Ejercicio 1: importar conexión en la BD. 
# Se importa utilizando la función connect a la ruta del archivo y después se asigna cursor a la conexión
conexion = sqlite3.connect('./Ejercicios/ejercicios-repaso-repaso/sqlite/sql-murder-mystery.db')
c = conexion.cursor()

# Ejercicio 2: extraer datos de la escena del crimen
# Se crea un texto con lenguaje sql para seleccionar todo lo relativo a la escena del crimen
query_csd = "select * from crime_scene_report"

# Se ejecuta la llamada anterior y se realiza un bucle con la respuesta para sacar toda la información
crime_scene_data = conexion.execute(query_csd).fetchall()
if crime_scene_data:
    print("\nÚltimo registro de la escena del crimen:")
    print(crime_scene_data[-1])
    print("\n")
# Ejercicio 3: datos de los testigos
query_id = "select * from interview"
interview_data = conexion.execute(query_id).fetchall()
if interview_data:
    print("\nÚltimos tres registros de los testigos que contienen la información más relevante:")
    for line in interview_data[-3:]:
        print(line)
    print("\n")

# Ejercicio 4: datos interrogatorios testigos
# De la búsqueda anterior se puede sacar información relevante:
## Un hombre con carnet oro en GFNG que empieza en 48Z y matrícula H42W corrió tras escucharse un disparo
## Otro testigo reconoce al asesino, también en el gimnasio, el día 09/01/2018
## El asesino dice que fue contratado por una mujer pelirroja con un Tesla Model S y mucho dinero. Mide al rededor de 65" o 67"

# Ejercicio 5: buscar sospechosos que indican los testigos
query_dlw = """select *
                from drivers_license
                where car_make = 'Tesla'
                and car_model = 'Model S'
                and gender = 'female'
                and height between 65 and 67
                and hair_color = 'red';"""
drivers_licence_women= conexion.execute(query_dlw).fetchall()
if drivers_licence_women:
    print("\nSospechosas de ser la mujer que encargó el asesinato:")
    for line in drivers_licence_women:
        print(line)
    print("\n")
# Esto devuelve tres resultados: 202298, 291182 y 918773

query_dlm = """select *
                from drivers_license
                where plate_number LIKE '%H42W%'
                and gender = 'male'"""
drivers_licence_men = conexion.execute(query_dlm).fetchall()
if drivers_licence_men:
    print("\nSospechosos de ser el hombre que corrió tras el disparo:")
    for line in drivers_licence_men:
        print(line)
    print("\n")

# Ejercicio 6: veamos qué dijo el sospechoso en el interrogatorio
query_ssn = "SELECT ssn FROM person WHERE license_id IN (202298, 291182, 918773)"
women_ssn = conexion.execute(query_ssn).fetchall()
if women_ssn:
    print("\nInformación de las sospechosas:")
    for line in women_ssn:
        print(line)
    print("\n")

# Ejercicio 7: encuentra al verdadero culpable


# Ejercicio 8: haz tus detenciones


conexion.close()