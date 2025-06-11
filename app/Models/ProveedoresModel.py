from db_init import get_connection

class ProveedorModel:
    def __init__(self, id, nombre, telefono, direccion, email):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.email = email

    def serializar(self):
        return self.__dict__

    @staticmethod
    def deserializar(data):
        return ProveedorModel(**data)

    @staticmethod
    def get_all():
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM proveedores")
        rows = cursor.fetchall()
        con.close()
        return [dict(zip(["id", "nombre", "telefono", "direccion", "email"], row)) for row in rows]

    @staticmethod
    def get_one(id):
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM proveedores WHERE id = ?", (id,))
        row = cursor.fetchone()
        con.close()
        return dict(zip(["id", "nombre", "telefono", "direccion", "email"], row)) if row else None

    def create(self):
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("""
            INSERT INTO proveedores (nombre, telefono, direccion, email)
            VALUES (?, ?, ?, ?)
        """, (self.nombre, self.telefono, self.direccion, self.email))
        con.commit()
        con.close()
        return True

    def update(self):
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("""
            UPDATE proveedores SET nombre=?, telefono=?, direccion=?, email=? WHERE id=?
        """, (self.nombre, self.telefono, self.direccion, self.email, self.id))
        con.commit()
        con.close()
        return True

    @staticmethod
    def delete(id):
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("DELETE FROM proveedores WHERE id = ?", (id,))
        con.commit()
        con.close()
        return True
