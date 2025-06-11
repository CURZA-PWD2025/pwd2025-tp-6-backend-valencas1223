from flask import Blueprint, request, jsonify

from app.Controllers.ProveedorController import ProveedorController

proveedor_bp = Blueprint('proveedores', __name__)

@proveedor_bp.route('/proveedores', methods=['GET'])
def get_all():
    return jsonify(ProveedorController.get_all())

@proveedor_bp.route('/proveedores/<int:id>', methods=['GET'])
def get_one(id):
    return jsonify(ProveedorController.get_one(id))

@proveedor_bp.route('/proveedores', methods=['POST'])
def create():
    data = request.json
    return jsonify(ProveedorController.create(data))

@proveedor_bp.route('/proveedores/<int:id>', methods=['PUT'])
def update(id):
    data = request.json
    data['id'] = id
    return jsonify(ProveedorController.update(data))

@proveedor_bp.route('/proveedores/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify(ProveedorController.delete(id))
