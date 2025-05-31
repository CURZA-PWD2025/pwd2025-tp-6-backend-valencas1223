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
        cursor.execute("SELECT * FROM articulos")
        rows = cursor.fetchall()
        con.close()
        return [dict(zip(["id", "descripcion", "precio", "stock", "marca_id", "proveedor_id"], row)) for row in rows]


    @staticmethod
    def get_one(id):
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM articulos WHERE id = ?", (id,))
        row = cursor.fetchone()
        con.close()
        return dict(zip(["id", "descripcion", "precio", "stock", "marca_id", "proveedor_id"], row)) if row else None


    def create(self):
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("""
            INSERT INTO articulos (descripcion, precio, stock, marca_id, proveedor_id)
            VALUES (?, ?, ?, ?, ?)
        """, (self.descripcion, self.precio, self.stock, self.marca_id, self.proveedor_id))
        con.commit()
        con.close()
        return True


    def update(self):
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("""
            UPDATE articulos SET descripcion=?, precio=?, stock=?, marca_id=?, proveedor_id=? WHERE id=?
        """, (self.descripcion, self.precio, self.stock, self.marca_id, self.proveedor_id, self.id))
        con.commit()
        con.close()
        return True


    @staticmethod
    def delete(id):
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("DELETE FROM articulos WHERE id = ?", (id,))
        con.commit()
        con.close()
        return True

