from flask import Blueprint, jsonify, request
from app.services import service_manager

person_routes = Blueprint('person', __name__)

@person_routes.route('/persons',methods=['POST'])
def create_product():
    data = request.get_json()
    usr = service_manager.person_service.create_person(data)
    return jsonify({'message': 'Person created', "Persona": usr.name}), 201

@person_routes.route('/persons', methods=['GET'])
def get_persons():
    return jsonify({"message": "Lista de personas"}), 200

