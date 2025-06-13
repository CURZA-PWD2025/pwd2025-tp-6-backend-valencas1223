# Controllers = get_all get_one create update delete 
from app.Models.MarcaModel import MarcaModel

class MarcaController:
    @staticmethod
    def get_all():
        marcas = MarcaModel.get_all()
        return [marca.serializar() for marca in marcas]

    @staticmethod
    def get_one(id):
        marca = MarcaModel.get_one(id)
        if marca:
            return marca.serializar()
        return {"error": "Marca no encontrada"}

    @staticmethod
    def create(data):
        try:
            marca = MarcaModel.deserializar(data)
            if marca.create():
                return {"message": "Marca creada", "marca": marca.serializar()}
            else:
                return {"error": "No se pudo crear la marca"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def update(id, data):
        try:
            marca = MarcaModel.get_one(id)
            if not marca:
                return {"error": "Marca no encontrada"}

            marca.nombre = data.get('nombre', marca.nombre)

            if marca.update():
                return {"message": "Marca actualizada", "marca": marca.serializar()}
            else:
                return {"error": "No se pudo actualizar la marca"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def delete(id):
        try:
            marca = MarcaModel.get_one(id)
            if not marca:
                return {"error": "Marca no encontrada"}

            if marca.delete():
                return {"message": "Marca eliminada"}
            else:
                return {"error": "No se pudo eliminar la marca"}
        except Exception as e:
            return {"error": str(e)}


