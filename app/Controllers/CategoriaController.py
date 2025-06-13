#Controllers = get_all get_one create update delete 
from app.Models.CategoriaModel import CategoriaModel

class CategoriaController:
    @staticmethod
    def get_all():
        return [categoria.serializar() for categoria in CategoriaModel.get_all()]

    @staticmethod
    def get_one(id):
        categoria = CategoriaModel.get_one(id)
        if categoria:
            return categoria.serializar()
        return {"error": "Categoría no encontrada"}

    @staticmethod
    def create(data):
        try:
            categoria = CategoriaModel.deserializar(data)
            if categoria.create():
                return {"message": "Categoría creada"}
            else:
                return {"error": "No se pudo crear la categoría"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def update(data):
        try:
            categoria = CategoriaModel.get_one(data.get('id'))
            if not categoria:
                return {"error": "Categoría no encontrada"}
            categoria.nombre = data.get('nombre', categoria.nombre)
            if categoria.update():
                return {"message": "Categoría actualizada"}
            else:
                return {"error": "No se pudo actualizar la categoría"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def delete(id):
        try:
            categoria = CategoriaModel.get_one(id)
            if not categoria:
                return {"error": "Categoría no encontrada"}
            if categoria.delete():
                return {"message": "Categoría eliminada"}
            else:
                return {"error": "No se pudo eliminar la categoría"}
        except Exception as e:
            return {"error": str(e)}

