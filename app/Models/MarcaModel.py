#Models =  get_all  get_one  create update delete serializar deserializar

from db_init import get_connection

class MarcaModel:
    def __init__(self, id=None, nombre=None):
        self.id = id
        self.nombre = nombre

    def serializar(self):
        return {"id": self.id, "nombre": self.nombre}

    @staticmethod
    def deserializar(data):
        return MarcaModel(id=data.get('id'), nombre=data.get('nombre'))

    @staticmethod
    def get_all():
        con = get_connection(with_db=True)
        cursor = con.cursor()
        cursor.execute("SELECT id, nombre FROM MARCAS")
        rows = cursor.fetchall()
        con.close()
        return [MarcaModel(*row) for row in rows]

    @staticmethod
    def get_one(id):
        con = get_connection(with_db=True)
        cursor = con.cursor()
        cursor.execute("SELECT id, nombre FROM MARCAS WHERE id = %s", (id,))
        row = cursor.fetchone()
        con.close()
        return MarcaModel(*row) if row else None

    def create(self):
        con = get_connection(with_db=True)
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO MARCAS (nombre) VALUES (%s)", (self.nombre,))
            con.commit()
            self.id = cursor.lastrowid
            return True
        except Exception as e:
            print(f"Error creando marca: {e}")
            return False
        finally:
            con.close()

    def update(self):
        con = get_connection(with_db=True)
        cursor = con.cursor()
        try:
            cursor.execute("UPDATE MARCAS SET nombre = %s WHERE id = %s", (self.nombre, self.id))
            con.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error actualizando marca: {e}")
            return False
        finally:
            con.close()

    def delete(self):
        con = get_connection(with_db=True)
        cursor = con.cursor()
        try:
            cursor.execute("DELETE FROM MARCAS WHERE id = %s", (self.id,))
            con.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error eliminando marca: {e}")
            return False
        finally:
            con.close()





