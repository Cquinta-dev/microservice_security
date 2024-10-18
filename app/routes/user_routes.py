from flask import Blueprint, jsonify, request
from app.services import service_manager
from ..schemas.user_schema import expected_fields_create

user_routes = Blueprint('user', __name__)

#Method for create users.
@user_routes.route('/createUser', methods=['POST'])
def create_user():
    try:
        data = request.get_json(force=True)

        if data is None:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        missing_fields = expected_fields_create - data.keys()
        if missing_fields:
            return jsonify({'error': 'Missing fields', 'missing': list(missing_fields)}), 400
        
        usr = service_manager.user_service.create_user(data)
        if usr is None:
            return jsonify({'error':'Person not found'}), 404
        
        return jsonify({'message': 'user created'}), 201
    
    except Exception as e:

        return jsonify({'error': 'Internal Server'}), 500  