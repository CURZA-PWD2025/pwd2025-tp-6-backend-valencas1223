#Models =  get_all  get_one  create update delete serializar deserializar

from db_init import get_connection


class ProveedorModel:
    def __init__(self, id, nombre, telefono, direccion, email):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.email = email

    def serializar(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "email": self.email
        }

    @staticmethod
    def deserializar(data):
        return ProveedorModel(
            id=data.get('id'),
            nombre=data.get('nombre'),
            telefono=data.get('telefono'),
            direccion=data.get('direccion'),
            email=data.get('email')
        )

    @staticmethod
    def get_all():
        try:
            with get_connection(with_db=True) as con:
                with con.cursor() as cursor:
                    cursor.execute("SELECT id, nombre, telefono, direccion, email FROM PROVEEDORES")
                    rows = cursor.fetchall()
                    return [ProveedorModel(*row) for row in rows]
        except Exception as e:
            print(f"Error al obtener proveedores: {e}")
            return []

    @staticmethod
    def get_one(id):
        con = get_connection(with_db=True)
        try:
            cursor = con.cursor()
            cursor.execute("SELECT id, nombre, telefono, direccion, email FROM PROVEEDORES WHERE id = %s", (id,))
            row = cursor.fetchone()
            return ProveedorModel(*row) if row else None
        finally:
            cursor.close()
            con.close()

    def create(self):
        con = get_connection(with_db=True)
        try:
            cursor = con.cursor()
            cursor.execute(
                "INSERT INTO PROVEEDORES (nombre, telefono, direccion, email) VALUES (%s, %s, %s, %s)",
                (self.nombre, self.telefono, self.direccion, self.email)
            )
            con.commit()
            self.id = cursor.lastrowid
            return self.id
        except Exception as e:
            print("Error al crear proveedor:", e)
            return None
        finally:
            cursor.close()
            con.close()

    def update(self):
        if self.id is None:
            print("Error: no se puede actualizar proveedor sin ID")
            return False
        con = get_connection(with_db=True)
        try:
            cursor = con.cursor()
            cursor.execute(
                "UPDATE PROVEEDORES SET nombre = %s, telefono = %s, direccion = %s, email = %s WHERE id = %s",
                (self.nombre, self.telefono, self.direccion, self.email, self.id)
            )
            con.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print("Error al actualizar proveedor:", e)
            return False
        finally:
            cursor.close()
            con.close()

    def delete(self):
        if self.id is None:
            print("Error: no se puede eliminar proveedor sin ID")
            return False
        con = get_connection(with_db=True)
        try:
            cursor = con.cursor()
            cursor.execute("DELETE FROM PROVEEDORES WHERE id = %s", (self.id,))
            con.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print("Error al eliminar proveedor:", e)
            return False
        finally:
            cursor.close()
            con.close()
