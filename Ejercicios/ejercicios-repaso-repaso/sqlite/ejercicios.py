import sqlite3

# Ejercicio 1: importar conexión en la BD. 
conexion = sqlite3.connect('./Ejercicios/ejercicios-repaso-repaso/sqlite/sql-murder-mystery.db')
c = conexion.cursor()

# Ejercicio 2: extraer datos de la escena del crimen
query_csd = "select * from crime_scene_report"

crime_scene_data = conexion.execute(query_csd).fetchall()
if crime_scene_data:
    print("\nÚltimo registro de la escena del crimen:")
    print(crime_scene_data[-1:])
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
print("""De la búsqueda anterior se puede sacar información relevante:
Un hombre con carnet oro en GFNG que empieza en 48Z y matrícula H42W corrió tras escucharse un disparo
Otro testigo reconoce al asesino, también en el gimnasio, el día 09/01/2018
El asesino dice que fue contratado por una mujer pelirroja con un Tesla Model S y mucho dinero. Mide al rededor de 65" o 67\n""")

# Ejercicio 5: buscar sospechosos que indican los testigos
query_dlm = """
    SELECT *
    FROM drivers_license
    WHERE plate_number LIKE '%H42W%'
      AND gender = 'male'
"""
drivers_licence_men = conexion.execute(query_dlm).fetchall()
if drivers_licence_men:
    print("\nSospechosos de ser el hombre que corrió tras el disparo:")
    for line in drivers_licence_men:
        print(line)
    print("\n")

    drivers_licence_m_ids = [row[0] for row in drivers_licence_men]

    if drivers_licence_m_ids:
        placeholders = ",".join(["?"] * len(drivers_licence_m_ids))

        query_person_membership = f"""
            SELECT p.id, p.name, g.membership_status
            FROM person AS p
            JOIN get_fit_now_member AS g
              ON p.id = g.person_id
            WHERE p.license_id IN ({placeholders})
        """

        male_suspect = conexion.execute(query_person_membership, drivers_licence_m_ids).fetchall()

        print("La persona sospechosa de ser el hombre que corrió tras el disparo es (id, name, membership_status):")
        for row in male_suspect:
            print(row)


# Ejercicio 6: veamos qué dijo el sospechoso en el interrogatorio

query_susw = f"select * from interview where person_id = {list(male_suspect[0])[0]}"

interview_suspect = conexion.execute(query_susw).fetchall()
if interview_suspect:
    print("\nLo que dijo el hombre sospechoso en el interrogatorio:")
    for line in interview_suspect:
        print(line)
    print("\n")
# Ejercicio 7: encuentra al verdadero culpable
query_dlw = """select *
                from drivers_license
                where car_make = 'Tesla'
                and car_model = 'Model S'
                and gender = 'female'
                and height between 65 and 67
                and hair_color = 'red';"""
drivers_licence_women = conexion.execute(query_dlw).fetchall()
if drivers_licence_women:
    print("\nSospechosas de ser la mujer que encargó el asesinato:")
    for line in drivers_licence_women:
        print(line)
    print("\n")
    drivers_licence_ids = [row[0] for row in drivers_licence_women]

if drivers_licence_ids:
    placeholders = ",".join(["?"] * len(drivers_licence_ids))

    query_person_income = f"""
        SELECT p.id, p.name, i.annual_income
        FROM person AS p
        JOIN income AS i ON p.ssn = i.ssn
        WHERE p.license_id IN ({placeholders})
        ORDER BY i.annual_income DESC
        LIMIT 1
    """

    women_info = conexion.execute(query_person_income, drivers_licence_ids).fetchall()
    female_suspect = {}
    if women_info:
        print("La mujer sospechosa de encargar el asesinato es (id, name, annual_income):")
        for row in women_info:
            female_suspect[row[0]] = row[1]
            print(row)
        print("\n")
# Ejercicio 8: haz tus detenciones

print(f"""Tras analizar la información, se ha llegado a la conclusión de que el culpable del asesinato es {list(male_suspect[0])[1]} y la mujer que lo encargó es {list(female_suspect.values())[0]}, por lo que se procedió a la detención de ambos.""")

conexion.close()