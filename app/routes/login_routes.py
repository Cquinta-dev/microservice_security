from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request
from ..services import service_manager
from ..schemas.user_schema import expected_fields_login

login_routes = Blueprint('auth', __name__)

#Method for login users.
@login_routes.route('/login', methods=['POST'])
def login():    

    try:
        data = request.get_json(force=True)
        if data is None:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        missing_fields = expected_fields_login - data.keys()
        if missing_fields:
            return jsonify({'error': 'Missing fields', 'missing': list(missing_fields)}), 400
        
        loginValidate = service_manager.login_service.validate_login(data)
        if loginValidate is None:            
            return jsonify({'error': 'User not found'}), 404
        elif loginValidate == 500:
            return jsonify({'error': 'Internal Server'}), 500   
        elif loginValidate == 401:
            return jsonify(message = 'Invalid credentials'), 401
        elif loginValidate == 402:
            return jsonify(message = 'User status inactive'), 400
        else:
            return jsonify(loginValidate), 200

    except Exception as e:
        print(e)
        return jsonify({'error': 'Internal Server'}), 500


#Method for refresh access token to endpoints.
@login_routes.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():

    current_user = get_jwt_identity()
    loginValidate = service_manager.login_service.refresh_token(current_user)
    if loginValidate:
        return jsonify(loginValidate), 200

    return jsonify({'error': 'Internal Server'}), 500


#Method for logout 
@login_routes.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    
    current_user = get_jwt_identity()
    saveLogout = service_manager.login_service.logout(current_user)
    if saveLogout:
        return jsonify(saveLogout), 200

    return jsonify({'error': 'Internal Server'}), 500


#Method for put users.
@login_routes.route('/resetPassword', methods=['PUT'])
def reset_password():

    try:
        data = request.get_json(force=True)
        if data is None:
            return jsonify({'error': 'No JSON data provided'}), 400

        missing_fields = expected_fields_login - data.keys()
        if missing_fields:
            return jsonify({'error': 'Missing fields', 'missing': list(missing_fields)}), 400
        
        userUpdate = service_manager.login_service.reset_password(data)
        if userUpdate is None:
            return jsonify({'error':'User not found'}), 404
        
        return jsonify({'message': 'Update password'}), 201

    except Exception as e:
        print(e)
        return jsonify({'error': 'Internal Server'}), 500