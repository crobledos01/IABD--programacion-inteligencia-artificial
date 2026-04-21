from abc import ABC, abstractmethod

# Interfaz
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

class MySQLAdapter(AdaptadorBaseDeDatos):
    
    def __init__(self, host, usuario, password, base_datos):
        self.host = host
        self.usuario = usuario
        self.password = password
        self.base_datos = base_datos
        self.conectado = False

    def conectar(self):
        self.conectado = True
        print(f"Conectando a MySQL en {self.host}, BD: {self.base_datos}")

    def ejecutar_consulta(self, consulta):
        if self.conectado:
            print(f"MySQL ejecutando consulta: {consulta}")
        else:
            print("Error: no hay conexión activa a MySQL")

    def cerrar_conexion(self):
        self.conectado = False
        print("Conexión MySQL cerrada")

class PostgreSQLAdapter(AdaptadorBaseDeDatos):
    
    def __init__(self, host, usuario, password, base_datos):
        self.host = host
        self.usuario = usuario
        self.password = password
        self.base_datos = base_datos
        self.conectado = False

    def conectar(self):
        self.conectado = True
        print(f"Conectando a PostgreSQL en {self.host}, BD: {self.base_datos}")

    def ejecutar_consulta(self, consulta):
        if self.conectado:
            print(f"PostgreSQL ejecutando consulta: {consulta}")
        else:
            print("Error: no hay conexión activa a PostgreSQL")

    def cerrar_conexion(self):
        self.conectado = False
        print("Conexión PostgreSQL cerrada")

class SQLiteAdapter(AdaptadorBaseDeDatos):
    
    def __init__(self, archivo_bd):
        self.archivo_bd = archivo_bd
        self.conectado = False

    def conectar(self):
        self.conectado = True
        print(f"Conectando a SQLite con el archivo: {self.archivo_bd}")

    def ejecutar_consulta(self, consulta):
        if self.conectado:
            print(f"SQLite ejecutando consulta: {consulta}")
        else:
            print("Error: no hay conexión activa a SQLite")

    def cerrar_conexion(self):
        self.conectado = False
        print("Conexión SQLite cerrada")


mysql = MySQLAdapter("localhost", "root", "1234", "empresa")
postgres = PostgreSQLAdapter("localhost", "admin", "abcd", "ventas")
sqlite = SQLiteAdapter("basedatos.db")

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