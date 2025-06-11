from flask import Blueprint, request, jsonify

from app.Controllers.Categoria_MarcaController import Categoria_MarcaController

marca_bp = Blueprint('marcas', __name__)

@marca_bp.route('/marcas', methods=['GET'])
def get_all():
    return jsonify(Categoria_MarcaController.get_all())

@marca_bp.route('/marcas/<int:id>', methods=['GET'])
def get_one(id):
    return jsonify(Categoria_MarcaController.get_one(id))

@marca_bp.route('/marcas', methods=['POST'])
def create():
    data = request.json
    return jsonify(Categoria_MarcaController.create(data))

@marca_bp.route('/marcas/<int:id>', methods=['PUT'])
def update(id):
    data = request.json
    data['id'] = id
    return jsonify(Categoria_MarcaController.update(data))

@marca_bp.route('/marcas/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify(Categoria_MarcaController.delete(id))
