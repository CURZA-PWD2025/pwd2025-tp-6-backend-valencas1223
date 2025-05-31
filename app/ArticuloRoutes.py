from flask import Blueprint, request, jsonify


from app.ArticuloController import ArticuloController

articulo_bp = Blueprint('articulos', __name__)

@articulo_bp.route('/articulos', methods=['GET'])
def get_all():
    return jsonify(ArticuloController.get_all())

@articulo_bp.route('/articulos/<int:id>', methods=['GET'])
def get_one(id):
    return jsonify(ArticuloController.get_one(id))

@articulo_bp.route('/articulos', methods=['POST'])
def create():
    data = request.json
    return jsonify(ArticuloController.create(data))

@articulo_bp.route('/articulos/<int:id>', methods=['PUT'])
def update(id):
    data = request.json
    data['id'] = id
    return jsonify(ArticuloController.update(data))

@articulo_bp.route('/articulos/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify(ArticuloController.delete(id))
