from flask import Blueprint, request, jsonify
from app.Controllers.MarcaController import MarcaController

marca_bp = Blueprint('marcas', __name__)

@marca_bp.route('/marcas', methods=['GET'])
def get_marcas():
    return jsonify(MarcaController.get_all())

@marca_bp.route('/marcas/<int:id>', methods=['GET'])
def get_marca(id):
    return jsonify(MarcaController.get_one(id))

@marca_bp.route('/marcas', methods=['POST'])
def create_marca():
    return jsonify(MarcaController.create(request.json))

@marca_bp.route('/marcas/<int:id>', methods=['PUT'])
def update_marca(id):
    # Pasamos id y json separados
    return jsonify(MarcaController.update(id, request.json))

@marca_bp.route('/marcas/<int:id>', methods=['DELETE'])
def delete_marca(id):
    return jsonify(MarcaController.delete(id))



