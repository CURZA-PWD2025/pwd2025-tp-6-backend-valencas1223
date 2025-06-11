import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME", "Negocio_de_Tencologias")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")

try:
    DB_PORT = int(DB_PORT)
except ValueError:
    DB_PORT = 3306

print("\nConectando a MySQL con la siguiente configuración:")
print(f"DB_NAME: {DB_NAME}")
print(f"DB_USER: {DB_USER}")
print(f"DB_PASSWORD: {DB_PASSWORD}")
print(f"DB_HOST: {DB_HOST}")
print(f"DB_PORT: {DB_PORT}\n")

DB_CONFIG = {
    'host': DB_HOST,
    'user': DB_USER,
    'password': DB_PASSWORD,
    'port': DB_PORT,
    'raise_on_warnings': True,
    'charset': 'utf8mb4',
}

TABLES = {}
SEEDS = {}

TABLES['MARCAS'] = (
    "CREATE TABLE `MARCAS` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `nombre` varchar(50) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") "
)
TABLES['CATEGORIAS'] = (
    "CREATE TABLE `CATEGORIAS` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `nombre` varchar(50) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") "
)
TABLES['PROVEEDORES'] = (
    "CREATE TABLE `PROVEEDORES` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `nombre` varchar(50) NOT NULL,"
    "  `telefono` varchar(50) NOT NULL,"
    "  `direccion` varchar(50) NOT NULL,"
    "  `email` varchar(50) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") "
)
TABLES['ARTICULOS'] = (
    "CREATE TABLE `ARTICULOS` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `descripcion` varchar(150) NOT NULL,"
    "  `precio` decimal(10,2) NOT NULL,"
    "  `stock` int(11) NOT NULL,"
    "  PRIMARY KEY (`id`),"
    "  `marca_id` int(11) NOT NULL,"
    "  `proveedor_id` int(11) NOT NULL,"
    "  FOREIGN KEY (`marca_id`) REFERENCES MARCAS(id),"
    "  FOREIGN KEY (`proveedor_id`) REFERENCES PROVEEDORES(id)"
    ") "
)
TABLES["ARTICULOS_CATEGORIAS"] = (
    "CREATE TABLE `ARTICULOS_CATEGORIAS` ("
    "  `articulo_id` int(11) NOT NULL,"
    "  `categoria_id` int(11) NOT NULL,"
    "  FOREIGN KEY (`articulo_id`) REFERENCES ARTICULOS(id),"
    "  FOREIGN KEY (`categoria_id`) REFERENCES CATEGORIAS(id)"
    ") "
)

SEEDS['PROVEEDORES'] = (
    "INSERT INTO PROVEEDORES (nombre, telefono, direccion, email) VALUES (%s, %s, %s, %s)",
    [
        ('Tech Solutions SRL', '1144556677', 'Av. Córdoba 1234, CABA', 'contacto@techsolutions.com.ar'),
        ('Informatica Total', '1167891234', 'Calle Falsa 456, Rosario', 'ventas@informatotal.com'),
        ('Redes & Cía', '1133445566', 'Av. San Martín 789, Mendoza', 'info@redesycia.com'),
        ('PC Express', '1122334455', 'Mitre 321, La Plata', 'soporte@pcexpress.com.ar'),
        ('DataSoft Argentina', '1198765432', 'Belgrano 987, Córdoba', 'contacto@datasoft.com.ar'),
        ('CompuMarket', '1177889900', 'Av. Rivadavia 4321, CABA', 'ventas@compumarket.com'),
        ('TechnoWorld', '1100112233', 'Urquiza 1111, Mar del Plata', 'info@technoworld.com.ar'),
        ('HardNet SRL', '1188997766', 'Alsina 654, Bahía Blanca', 'clientes@hardnet.com'),
        ('BitWare', '1155667788', 'Av. Colon 2020, Salta', 'bitware@correo.com'),
        ('Digital Point', '1133221100', 'San Juan 3030, Tucumán', 'digital@dp.com.ar')
    ]
)
SEEDS['MARCAS'] = (
    "INSERT INTO MARCAS (nombre) VALUES (%s)",
    [
        ('HP',),
        ('Dell',),
        ('Lenovo',),
        ('Asus',),
        ('Acer',),
        ('Apple',),
        ('Samsung',),
        ('LG',),
        ('Sony',),
        ('Toshiba',)
    ]
)
SEEDS['CATEGORIAS'] = (
    "INSERT INTO CATEGORIAS (nombre) VALUES (%s)",
    [
        ('Notebooks y Laptops',),
        ('Computadoras de Escritorio',),
        ('Tablets',),
        ('Monitores',),
        ('Impresoras',),
        ('Periféricos',),
        ('Redes y Conectividad',),
        ('Almacenamiento',),
        ('Software',),
        ('Componentes',)
    ]
)
SEEDS['ARTICULOS'] = (
    "INSERT INTO ARTICULOS (descripcion, precio, stock, marca_id, proveedor_id) VALUES (%s, %s, %s, %s, %s)",
    [
        ('Notebook HP Pavilion 15.6" i5 8GB RAM 512GB SSD', 450000.00, 12, 1, 1),
        ('PC de Escritorio Dell OptiPlex i7 16GB RAM 1TB HDD', 520000.00, 7, 2, 2),
        ('Tablet Lenovo M10 HD 10.1" 32GB WiFi', 190000.00, 25, 3, 3),
        ('Monitor Asus ProArt 27" 4K UHD IPS', 330000.00, 9, 4, 4),
        ('Impresora Láser HP LaserJet Pro M404dn', 240000.00, 6, 1, 5),
        ('Mouse Logitech M185 Inalámbrico', 8900.00, 60, 6, 6),
        ('Router TP-Link Archer C6 AC1200', 21000.00, 35, 7, 7),
        ('Disco Externo Seagate 2TB USB 3.0', 45000.00, 20, 8, 8),
        ('Microsoft Office 365 Personal - Licencia 1 año', 18000.00, 15, 9, 9),
        ('Memoria RAM Corsair Vengeance 8GB DDR4 3200MHz', 32000.00, 30, 10, 10)
    ]
)

SEEDS['ARTICULOS_CATEGORIAS'] = (
    "INSERT INTO ARTICULOS_CATEGORIAS (articulo_id, categoria_id) VALUES (%s, %s)",
    [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10)
    ]
)


def Portable_Database(cursor):
    cursor.execute(
        f"CREATE DATABASE IF NOT EXISTS {DB_NAME} DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
    )
    print(f" Base de datos '{DB_NAME}' creada correctamente.")


def create_tables(tables, cursor):
    for table_name, table_sql in tables.items():
        try:
            cursor.execute(table_sql)
            print(f" Tabla '{table_name}' verificada o creada correctamente.")
        except Error as err:
            print(f" Advertencia al crear la tabla '{table_name}': {err.msg}")


def seeds_tables(seeds, cursor):
    for table_name, (sql, data) in seeds.items():
        try:
            cursor.executemany(sql, data)
            print(f" Datos insertados en '{table_name}' correctamente.")
        except Error as err:
            print(f" Error al insertar datos en '{table_name}': {err.msg}")
            
def get_connection(with_db=False):
    config = DB_CONFIG.copy()
    if with_db:
        config['database'] = DB_NAME
    return mysql.connector.connect(**config)

if __name__ == "__main__":
    try:
        cnx = get_connection(with_db=False)
        cursor = cnx.cursor()
        Portable_Database(cursor)  
    except Error as e:
        print(f" Error al conectar o crear la base de datos: {e}")
    finally:
        cursor.close()
        cnx.close()

    try:
        cnx = get_connection(with_db=True)
        cursor = cnx.cursor()
        create_tables(TABLES, cursor)
        seeds_tables(SEEDS, cursor)
        cnx.commit()
    except Error as e:
        print(f"Error al crear tablas o insertar datos: {e}")
    finally:
        cursor.close()
        cnx.close()