#Controllers = get_all get_one create update delete 

from app.Models.ArticuloModel import ArticuloModel

class ArticuloController:
    @staticmethod
    def get_all():
        return ArticuloModel.get_all()

    @staticmethod
    def get_one(id):
        articulo = ArticuloModel.get_one(id)
        if articulo:
            return articulo
        return {"error": "Artículo no encontrado"}

    @staticmethod
    def create(data):
        try:
            articulo = ArticuloModel.deserializar(data)
            articulo.create()
            return {"message": "Artículo creado"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def update(data):
        try:
            articulo = ArticuloModel.deserializar(data)
            articulo.update()
            return {"message": "Artículo actualizado"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def delete(id):
        try:
            ArticuloModel.delete(id)
            return {"message": "Artículo eliminado"}
        except Exception as e:
            return {"error": str(e)}
