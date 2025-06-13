# Models = get_all  get_one  create  update  delete  serializar  deserializar

from db_init import get_connection
from app.Models.MarcaModel import MarcaModel
from app.Models.ProveedoresModel import ProveedorModel
from app.Models.CategoriaModel import CategoriaModel

class ArticuloModel:
    def __init__(self, id, descripcion, precio, stock, marca: MarcaModel, proveedor: ProveedorModel, categoria: CategoriaModel):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca = marca
        self.proveedor = proveedor
        self.categoria = categoria

    def serializar(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock,
            "marca": self.marca.serializar(),
            "proveedor": self.proveedor.serializar(),
            "categoria": self.categoria.serializar()
        }

    @staticmethod
    def deserializar(data):
        marca = MarcaModel.deserializar(data['marca'])
        proveedor = ProveedorModel.deserializar(data['proveedor'])
        categoria = CategoriaModel.deserializar(data['categoria'])
        return ArticuloModel(data.get('id'), data['descripcion'], data['precio'], data['stock'], marca, proveedor, categoria)

    @staticmethod
    def get_all():
        con = get_connection(with_db=True)
        cursor = con.cursor()
        cursor.execute("""
            SELECT a.id, a.descripcion, a.precio, a.stock,
                   m.id, m.nombre,
                   p.id, p.nombre, p.telefono, p.direccion, p.email,
                   c.id, c.nombre
            FROM articulos a
            JOIN marcas m ON a.marca_id = m.id
            JOIN proveedores p ON a.proveedor_id = p.id
            JOIN articulos_categorias ac ON a.id = ac.articulo_id
            JOIN categorias c ON ac.categoria_id = c.id
        """)
        rows = cursor.fetchall()
        con.close()
        articulos = []
        for row in rows:
            marca = MarcaModel(row[4], row[5])
            proveedor = ProveedorModel(row[6], row[7], row[8], row[9], row[10])
            categoria = CategoriaModel(row[11], row[12])
            articulo = ArticuloModel(row[0], row[1], row[2], row[3], marca, proveedor, categoria)
            articulos.append(articulo.serializar())
        return articulos

    @staticmethod
    def get_one(id):
        con = get_connection(with_db=True)
        cursor = con.cursor()
        cursor.execute("""
            SELECT a.id, a.descripcion, a.precio, a.stock,
                   m.id, m.nombre,
                   p.id, p.nombre, p.telefono, p.direccion, p.email,
                   c.id, c.nombre
            FROM articulos a
            JOIN marcas m ON a.marca_id = m.id
            JOIN proveedores p ON a.proveedor_id = p.id
            JOIN articulos_categorias ac ON a.id = ac.articulo_id
            JOIN categorias c ON ac.categoria_id = c.id
            WHERE a.id = %s
        """, (id,))
        row = cursor.fetchone()
        con.close()
        if row:
            marca = MarcaModel(row[4], row[5])
            proveedor = ProveedorModel(row[6], row[7], row[8], row[9], row[10])
            categoria = CategoriaModel(row[11], row[12])
            articulo = ArticuloModel(row[0], row[1], row[2], row[3], marca, proveedor, categoria)
            return articulo.serializar()
        return None

    def create(self):
        con = get_connection(with_db=True)
        cursor = con.cursor()
        
        cursor.execute("""
            INSERT INTO articulos (descripcion, precio, stock, marca_id, proveedor_id)
            VALUES (%s, %s, %s, %s, %s)
        """, (self.descripcion, self.precio, self.stock, self.marca.id, self.proveedor.id))
        articulo_id = cursor.lastrowid
       
        cursor.execute("""
            INSERT INTO articulos_categorias (articulo_id, categoria_id)
            VALUES (%s, %s)
        """, (articulo_id, self.categoria.id))
        con.commit()
        con.close()
        self.id = articulo_id  

    def update(self):
        con = get_connection(with_db=True)
        cursor = con.cursor()
        cursor.execute("""
            UPDATE articulos
            SET descripcion = %s, precio = %s, stock = %s,
                marca_id = %s, proveedor_id = %s
            WHERE id = %s
        """, (self.descripcion, self.precio, self.stock, self.marca.id, self.proveedor.id, self.id))
    
        cursor.execute("""
            DELETE FROM articulos_categorias WHERE articulo_id = %s
        """, (self.id,))
        cursor.execute("""
            INSERT INTO articulos_categorias (articulo_id, categoria_id)
            VALUES (%s, %s)
        """, (self.id, self.categoria.id))
        con.commit()
        con.close()

    @staticmethod
    def delete(id):
        con = get_connection(with_db=True)
        cursor = con.cursor()
    
        cursor.execute("DELETE FROM articulos_categorias WHERE articulo_id = %s", (id,))
        cursor.execute("DELETE FROM articulos WHERE id = %s", (id,))
        con.commit()
        con.close()


