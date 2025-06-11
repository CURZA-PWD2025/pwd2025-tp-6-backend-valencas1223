from app.Models.ProveedoresModel import ProveedorModel

class ProveedorController:
    @staticmethod
    def get_all():
        return ProveedorModel.get_all()

    @staticmethod
    def get_one(id):
        return ProveedorModel.get_one(id)

    @staticmethod
    def create(data):
        proveedor = ProveedorModel.deserializar(data)
        proveedor.create()
        return {"message": "Proveedor creado"}

    @staticmethod
    def update(data):
        proveedor = ProveedorModel.deserializar(data)
        proveedor.update()
        return {"message": "Proveedor actualizado"}

    @staticmethod
    def delete(id):
        ProveedorModel.delete(id)
        return {"message": "Proveedor eliminado"}
