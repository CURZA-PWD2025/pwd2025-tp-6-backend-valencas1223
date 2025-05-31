from app.ArticuloModel import ArticuloModel

class ArticuloController:
    @staticmethod
    def get_all():
        return ArticuloModel.get_all()

    @staticmethod
    def get_one(id):
        return ArticuloModel.get_one(id)

    @staticmethod
    def create(data):
        articulo = ArticuloModel.deserializar(data)
        articulo.create()
        return {"message": "Artículo creado"}

    @staticmethod
    def update(data):
        articulo = ArticuloModel.deserializar(data)
        articulo.update()
        return {"message": "Artículo actualizado"}

    @staticmethod
    def delete(id):
        ArticuloModel.delete(id)
        return {"message": "Artículo eliminado"}
