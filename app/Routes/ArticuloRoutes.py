from flask import Blueprint, request, jsonify
from app.Controllers.ArticuloController import ArticuloController

articulo_bp = Blueprint('articulos', __name__)

@articulo_bp.route('/articulos', methods=['GET'])
def get_articulos():
    return jsonify(ArticuloController.get_all())

@articulo_bp.route('/articulos/<int:id>', methods=['GET'])
def get_articulo(id):
    return jsonify(ArticuloController.get_one(id))

@articulo_bp.route('/articulos', methods=['POST'])
def create_articulo():
    return jsonify(ArticuloController.create(request.json))

@articulo_bp.route('/articulos/<int:id>', methods=['PUT'])
def update_articulo(id):
    data = request.json
    data['id'] = id
    return jsonify(ArticuloController.update(data))

@articulo_bp.route('/articulos/<int:id>', methods=['DELETE'])
def delete_articulo(id):
    return jsonify(ArticuloController.delete(id))
