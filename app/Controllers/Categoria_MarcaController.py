from app.Models.Categoria_MarcaModel import Categoria_MarcaModel

class Categoria_MarcaController:
    @staticmethod
    def get_all():
        return Categoria_MarcaModel.get_all()

    @staticmethod
    def get_one(id):
        return Categoria_MarcaModel.get_one(id)

    @staticmethod
    def create(data):
        marca = Categoria_MarcaModel.deserializar(data)
        marca.create()
        return {"message": "Marca creada"}

    @staticmethod
    def update(data):
        marca = Categoria_MarcaModel.deserializar(data)
        marca.update()
        return {"message": "Marca actualizada"}

    @staticmethod
    def delete(id):
        Categoria_MarcaModel.delete(id)
        return {"message": "Marca eliminada"}
