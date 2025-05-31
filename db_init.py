import mysql.connector

from mysql.connector import Error, errorcode

import os

from dotenv import load_dotenv

load_dotenv()

print("DB_NAME:", os.getenv("DB_NAME"))
print("DB_USER:", os.getenv("DB_USER"))
print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_PORT:", os.getenv("DB_PORT"))


DB_NAME = os.getenv("DB_NAME", "tienda")

DB_CONFIG = {
    'host': os.getenv("DB_HOST", "localhost"),
    'user': os.getenv("DB_USER", "root"),
    'password': os.getenv("DB_PASSWORD", ""),
    'port': int(os.getenv("DB_PORT", "3306")), 
    'raise_on_warnings': True,
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
    " `precio` decimal(10,2) NOT NULL,"
    "  `stock` int(11) NOT NULL,"
    "  PRIMARY KEY (`id`),"
    "  `marca_id` int(11) NOT NULL,"
    "  `proveedor_id` int(11) NOT NULL,"
    " foreign key (`marca_id`) references MARCAS(id),"
    " foreign key (`proveedor_id`) references PROVEEDORES(id)"
    ") "
)
TABLES["ARTICULOS_CATEGORIAS"] = (
    "CREATE TABLE `ARTICULOS_CATEGORIAS` ("
    "  `articulo_id` int(11) NOT NULL,"
    "  `categoria_id` int(11) NOT NULL,"
    " foreign key (`articulo_id`) references ARTICULOS(id),"
    " foreign key (`categoria_id`) references CATEGORIAS(id)"
    ") "
)

SEEDS['PROVEEDORES'] = (
    "INSERT INTO PROVEEDORES (nombre, telefono, direccion, email) "
    "VALUES (%s, %s, %s, %s)",
    [
        ('Tech Solutions SRL', '1144556677',
         'Av. Córdoba 1234, CABA', 'contacto@techsolutions.com.ar'),
        ('Informatica Total', '1167891234',
         'Calle Falsa 456, Rosario', 'ventas@informatotal.com'),
        ('Redes & Cía', '1133445566',
         'Av. San Martín 789, Mendoza', 'info@redesycia.com'),
        ('PC Express', '1122334455', 'Mitre 321, La Plata', 'soporte@pcexpress.com.ar'),
        ('DataSoft Argentina', '1198765432',
         'Belgrano 987, Córdoba', 'contacto@datasoft.com.ar'),
        ('CompuMarket', '1177889900',
         'Av. Rivadavia 4321, CABA', 'ventas@compumarket.com'),
        ('TechnoWorld', '1100112233',
         'Urquiza 1111, Mar del Plata', 'info@technoworld.com.ar'),
        ('HardNet SRL', '1188997766',
         'Alsina 654, Bahía Blanca', 'clientes@hardnet.com'),
        ('BitWare', '1155667788', 'Av. Colon 2020, Salta', 'bitware@correo.com'),
        ('Digital Point', '1133221100', 'San Juan 3030, Tucumán', 'digital@dp.com.ar')
    ]
)
SEEDS['MARCAS'] = (
    "INSERT INTO MARCAS (nombre) "
    "VALUES (%s)",
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
    "INSERT INTO CATEGORIAS (nombre) "
    "VALUES (%s)",
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
    "INSERT INTO ARTICULOS (descripcion, precio, stock, marca_id, proveedor_id) "
    "VALUES (%s, %s, %s, %s, %s)",
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
    "INSERT INTO ARTICULOS_CATEGORIAS (articulo_id, categoria_id) "
    "VALUES (%s, %s)",
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
    ])


def create_database(cursor):
    try:
        cursor.execute(
            f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8'", )
    except Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database already exists")
        else:
            print(err)
    else:
        print(f"Database {DB_NAME} created successfully.")


def create_tables(tables, cursor):

    for table_name in tables:
        table_description = tables[table_name]
        try:
            print(f"Creating table {table_name}: ", end="")
            cursor.execute(table_description)
        except Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")


def seeds_tables(seed, cursor):
    for table_name in seed:
        seed_description = seed[table_name]
        try:
            print(f"Seeding table {table_name}: ", end="")
            cursor.executemany(seed_description[0], seed_description[1])
        except Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")


cxn = mysql.connector.connect(**DB_CONFIG)

cursor = cxn.cursor()

create_database(cursor)

cursor.close()

cxn.close()




CONF_DB = DB_CONFIG.copy()

CONF_DB['database'] = DB_NAME

cxn = mysql.connector.connect(**CONF_DB)

cursor = cxn.cursor()



create_tables(TABLES, cursor)
seeds_tables(SEEDS, cursor)



cxn.commit()

cursor.close()

cxn.close()