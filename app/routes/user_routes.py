from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request
from app.services import service_manager
from ..schemas.user_schema import expected_fields_create
from ..schemas.user_schema import expected_fields_update

user_routes = Blueprint('user', __name__)

#Method for create users.
@user_routes.route('/createUser', methods=['POST'])
@jwt_required()
def create_user():
    
    try:
        data = request.get_json(force=True)
        if data is None:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        missing_fields = expected_fields_create - data.keys()
        if missing_fields:
            return jsonify({'error': 'Missing fields', 'missing': list(missing_fields)}), 400
        
        usr = service_manager.user_service.create_user(data, get_jwt_identity())
        if usr is None:
            return jsonify({'error':'Person not found'}), 404
        
        return jsonify({'message': 'user created'}), 201
    
    except Exception as e:
        print(e)
        return jsonify({'error': 'Internal Server'}), 500  
    

#Method for get users.
@user_routes.route('/getUser', methods=['GET'])    
@jwt_required()
def get_user():
    usrId = request.args.get('id')

    if usrId is None:
        return jsonify({'error': 'Id was not provided'}), 400
    
    usr = service_manager.user_service.get_user(usrId)
    if usr is None:
        return jsonify({'error':'User not found'}), 404
    
    return jsonify(usr), 200


#Method for put users.
@user_routes.route('/updateUser', methods=['PUT'])
@jwt_required()
def update_user():

    try:
        data = request.get_json(force=True)
        if data is None:
            return jsonify({'error': 'No JSON data provided'}), 400

        missing_fields = expected_fields_update - data.keys()
        if missing_fields:
            return jsonify({'error': 'Missing fields', 'missing': list(missing_fields)}), 400
        
        userUpdate = service_manager.user_service.update_user(data, get_jwt_identity())
        if userUpdate is None:
            return jsonify({'error':'User not found'}), 404
        
        return jsonify({'message': 'user update'}), 201

    except Exception as e:
        print(e)
        return jsonify({'error': 'Internal Server'}), 500