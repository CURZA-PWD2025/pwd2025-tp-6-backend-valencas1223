from flask import Blueprint, request, jsonify
from app.Controllers.CategoriaController import CategoriaController

categoria_bp = Blueprint('categorias', __name__)

@categoria_bp.route('/categorias', methods=['GET'])
def get_categorias():
    return jsonify(CategoriaController.get_all())

@categoria_bp.route('/categorias/<int:id>', methods=['GET'])
def get_categoria(id):
    return jsonify(CategoriaController.get_one(id))

@categoria_bp.route('/categorias', methods=['POST'])
def create_categoria():
    return jsonify(CategoriaController.create(request.json))

@categoria_bp.route('/categorias/<int:id>', methods=['PUT'])
def update_categoria(id):
    data = request.json
    data['id'] = id
    return jsonify(CategoriaController.update(data))

@categoria_bp.route('/categorias/<int:id>', methods=['DELETE'])
def delete_categoria(id):
    return jsonify(CategoriaController.delete(id))

