from db_init import get_connection

class ArticuloModel:
    def __init__(self, id, descripcion, precio, stock, marca_id, proveedor_id):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca_id = marca_id
        self.proveedor_id = proveedor_id

    def serializar(self):
        return self.__dict__

    @staticmethod
    def deserializar(data):
        return ArticuloModel(**data)

    @staticmethod
    def get_all():
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("""
            SELECT a.id, a.descripcion, a.precio, a.stock, 
                   m.id AS marca_id, m.descripcion AS marca,
                   p.id AS proveedor_id, p.nombre AS proveedor
            FROM articulos a
            JOIN marcas m ON a.marca_id = m.id
            JOIN proveedores p ON a.proveedor_id = p.id
        """)
        rows = cursor.fetchall()
        con.close()
        return [
            {
                "id": row[0],
                "descripcion": row[1],
                "precio": row[2],
                "stock": row[3],
                "marca_id": row[4],
                "marca": row[5],
                "proveedor_id": row[6],
                "proveedor": row[7]
            }
            for row in rows
        ]

    @staticmethod
    def get_one(id):
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("""
            SELECT a.id, a.descripcion, a.precio, a.stock, 
                   m.id AS marca_id, m.descripcion AS marca,
                   p.id AS proveedor_id, p.nombre AS proveedor
            FROM articulos a
            JOIN marcas m ON a.marca_id = m.id
            JOIN proveedores p ON a.proveedor_id = p.id
            WHERE a.id = %s
        """, (id,))
        row = cursor.fetchone()
        con.close()
        if row:
            return {
                "id": row[0],
                "descripcion": row[1],
                "precio": row[2],
                "stock": row[3],
                "marca_id": row[4],
                "marca": row[5],
                "proveedor_id": row[6],
                "proveedor": row[7]
            }
        return None

    def create(self):
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("""
            INSERT INTO articulos (descripcion, precio, stock, marca_id, proveedor_id)
            VALUES (%s, %s, %s, %s, %s)
        """, (self.descripcion, self.precio, self.stock, self.marca_id, self.proveedor_id))
        con.commit()
        con.close()
        return True

    def update(self):
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("""
            UPDATE articulos 
            SET descripcion=%s, precio=%s, stock=%s, marca_id=%s, proveedor_id=%s 
            WHERE id=%s
        """, (self.descripcion, self.precio, self.stock, self.marca_id, self.proveedor_id, self.id))
        con.commit()
        con.close()
        return True

    @staticmethod
    def delete(id):
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("DELETE FROM articulos WHERE id = %s", (id,))
        con.commit()
        con.close()
        return True



