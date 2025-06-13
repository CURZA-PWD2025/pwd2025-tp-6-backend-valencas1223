#Controllers = get_all get_one create update delete 

from app.Models.ProveedoresModel import ProveedorModel

class ProveedorController:
    @staticmethod
    def get_all():
        proveedores = ProveedorModel.get_all()
        return [p.serializar() for p in proveedores]

    @staticmethod
    def get_one(id):
        proveedor = ProveedorModel.get_one(id)
        if proveedor:
            return proveedor.serializar()
        return {"error": "Proveedor no encontrado"}

    @staticmethod
    def create(data):
        try:
            proveedor = ProveedorModel.deserializar(data)
            if proveedor.create():
                return {"message": "Proveedor creado", "proveedor": proveedor.serializar()}
            else:
                return {"error": "No se pudo crear el proveedor"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def update(data):
        try:
            proveedor = ProveedorModel.get_one(data.get("id"))
            if not proveedor:
                return {"error": "Proveedor no encontrado"}

            proveedor.nombre = data.get("nombre", proveedor.nombre)
            proveedor.telefono = data.get("telefono", proveedor.telefono)
            proveedor.direccion = data.get("direccion", proveedor.direccion)
            proveedor.email = data.get("email", proveedor.email)

            if proveedor.update():
                return {"message": "Proveedor actualizado", "proveedor": proveedor.serializar()}
            else:
                return {"error": "No se pudo actualizar el proveedor"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def delete(id):
        try:
            proveedor = ProveedorModel.get_one(id)
            if not proveedor:
                return {"error": "Proveedor no encontrado"}

            if proveedor.delete():
                return {"message": "Proveedor eliminado"}
            else:
                return {"error": "No se pudo eliminar el proveedor"}
        except Exception as e:
            return {"error": str(e)}

