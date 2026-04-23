from abc import ABC, abstractmethod

# Clase AdaptadorBaseDeDatos
# Se crea la interfaz común para los 3 adaptadores de base de datos
class AdaptadorBaseDeDatos(ABC):
    
    @abstractmethod
    def conectar(self):
        pass

    @abstractmethod
    def ejecutar_consulta(self, consulta):
        pass

    @abstractmethod
    def cerrar_conexion(self):
        pass

# Clase DapatadorSQL
# Implementa la interfaz para SQL, necesita host, usuario, password y base de datos para conectarse
# Cada método llama a la interfaz general y muestra un mensaje para cada acción
class AdaptadorSQL(AdaptadorBaseDeDatos):
    
    def __init__(self, host, usuario, password, base_datos):
        self.host = host
        self.usuario = usuario
        self.password = password
        self.base_datos = base_datos
        self.conectado = False

    def conectar(self):
        self.conectado = True
        print("Conectado a MySQL")

    def ejecutar_consulta(self, consulta):
        if self.conectado:
            print(f"MySQL está ejecutando la consulta: {consulta}")
        else:
            print("Error en la consulta de MySQL")

    def cerrar_conexion(self):
        self.conectado = False
        print("Se ha cerrado la conexión a MySQL")

# Clase AdaptadorPostgre
# Implementa la interfaz para PostgreSQL, necesita host, usuario, password y base de datos para conectarse
# Cada método llama a la interfaz general y muestra un mensaje para cada acción
class AdaptadorPostgre(AdaptadorBaseDeDatos):
    
    def __init__(self, host, usuario, password, base_datos):
        self.host = host
        self.usuario = usuario
        self.password = password
        self.base_datos = base_datos
        self.conectado = False

    def conectar(self):
        self.conectado = True
        print(f"Conectado a PostgreSQL")

    def ejecutar_consulta(self, consulta):
        if self.conectado:
            print(f"PostgreSQL está ejecutando la consulta: {consulta}")
        else:
            print("Error en la consulta de PostgreSQL")

    def cerrar_conexion(self):
        self.conectado = False
        print("Se ha cerrado la conexión a PostgreSQL")

# Clase AdaptadorSQLite
# Implementa la interfaz para SQLite, necesita el archivo de base de datos para conectarse
# Cada método llama a la interfaz general y muestra un mensaje para cada acción
class AdaptadorSQLite(AdaptadorBaseDeDatos):
    
    def __init__(self, archivo_bd):
        self.archivo_bd = archivo_bd
        self.conectado = False

    def conectar(self):
        self.conectado = True
        print(f"Conectado a SQLite")

    def ejecutar_consulta(self, consulta):
        if self.conectado:
            print(f"SQLite está ejecutando la consulta: {consulta}")
        else:
            print("Error en la consulta de SQLite")

    def cerrar_conexion(self):
        self.conectado = False
        print("Se ha cerrado la conexión a SQLite")

# Se crean los adaptadores de cada base de datos con los parámetros necesarios de cada uno
mysql = AdaptadorSQL("localhost", "root", "1234", "empresa")
postgres = AdaptadorPostgre("localhost", "admin", "abcd", "ventas")
sqlite = AdaptadorSQLite("basedatos.db")

# Se llaman a los métodos de cada uno de los adaptadores
mysql.conectar()
mysql.ejecutar_consulta("SELECT * FROM clientes")
mysql.cerrar_conexion()

print("-----")

postgres.conectar()
postgres.ejecutar_consulta("SELECT * FROM productos")
postgres.cerrar_conexion()

print("-----")

sqlite.conectar()
sqlite.ejecutar_consulta("SELECT * FROM empleados")
sqlite.cerrar_conexion()