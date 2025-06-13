from flask import Blueprint, request, jsonify
from app.Controllers.ProveedorController import ProveedorController

proveedor_bp = Blueprint('proveedores', __name__)

@proveedor_bp.route('/proveedores', methods=['GET'])
def get_proveedores():
    return jsonify(ProveedorController.get_all())

@proveedor_bp.route('/proveedores/<int:id>', methods=['GET'])
def get_proveedor(id):
    return jsonify(ProveedorController.get_one(id))

@proveedor_bp.route('/proveedores', methods=['POST'])
def create_proveedor():
    return jsonify(ProveedorController.create(request.json))

@proveedor_bp.route('/proveedores/<int:id>', methods=['PUT'])
def update_proveedor(id):
    data = request.json
    data['id'] = id
    return jsonify(ProveedorController.update(data))

@proveedor_bp.route('/proveedores/<int:id>', methods=['DELETE'])
def delete_proveedor(id):
    return jsonify(ProveedorController.delete(id))
