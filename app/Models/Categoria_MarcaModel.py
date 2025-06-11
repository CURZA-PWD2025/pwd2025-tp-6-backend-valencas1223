from db_init import get_connection


class Categoria_MarcaModel:
    def __init__(self, id, descripcion):
        self.id = id
        self.descripcion = descripcion
        
        def serializar(self):
            return self.__dict__
        
        
        
        @staticmethod
        def deserializar(data):
            return Categoria_MarcaModel(**data)
        
    @staticmethod
    def get_all():
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM marcas")
        rows = cursor.fetchall()
        con.close()
        return [dict(zip(["id", "descripcion"], row)) for row in rows]

    @staticmethod
    def get_one(id):
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM marcas WHERE id = ?", (id,))
        row = cursor.fetchone()
        con.close()
        return dict(zip(["id", "descripcion"], row)) if row else None

    def create(self):
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("INSERT INTO marcas (descripcion) VALUES (?)", (self.descripcion,))
        con.commit()
        con.close()
        return True

    def update(self):
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("UPDATE marcas SET descripcion=? WHERE id=?", (self.descripcion, self.id))
        con.commit()
        con.close()
        return True

    @staticmethod
    def delete(id):
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("DELETE FROM marcas WHERE id = ?", (id,))
        con.commit()
        con.close()
        return True    
        
        