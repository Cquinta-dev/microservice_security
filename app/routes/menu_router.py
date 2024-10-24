from flask_jwt_extended import jwt_required, get_jwt_identity
from ..schemas.menu_schema import expected_fields_create
from ..schemas.menu_schema import expected_fields_udpate
from flask import Blueprint, jsonify, request
from ..services import service_manager
from ..utils.constants import constants

menu_router = Blueprint('menu', __name__)

#Method for create menu.
@menu_router.route('/createMenu', methods=['POST'])
@jwt_required()
def create_menu():

    data = request.get_json(force=True)
    if data is None:
        return jsonify({'error': constants.NOT_JSON}), 400
    
    missing_fields = expected_fields_create - data.keys()
    if missing_fields:
        return jsonify({'error': constants.NOT_FIELDS, 'missing': list(missing_fields)}), 400
    
    createMenu = service_manager.menu_service.create_menu(data, get_jwt_identity())
    if createMenu is None:
        return jsonify({'error': constants.INTERNAL_ERROR}), 500   
    
    return jsonify({'message': createMenu}), 201


#Method for get list to menu.
@menu_router.route('/allMenu', methods=['GET'])
@jwt_required()
def get_menus():

    allMenus = service_manager.menu_service.get_departaments()
    if allMenus is None:
        return jsonify({'error': constants.NOT_FOUND_LIST}), 404

    return jsonify(allMenus), 200    


#Method for get combo menu.
@menu_router.route('/getComboMenu', methods=['GET'])
@jwt_required()
def get_combo_menu():

    id = request.args.get('id')
    if id is None: 
        return jsonify({'error': constants.NOT_ID}), 400    
    
    getMenu = service_manager.menu_service.get_combo_menu(id)
    if getMenu is None:
        return jsonify({'error': constants.NOT_FOUND_LIST}), 404

    return jsonify(getMenu), 200


#Method for udpate menu.
@menu_router.route('/updateMenu', methods=['PUT'])
@jwt_required()
def update_person():    
        
    data = request.get_json(force=True)
    if data is None:
        return jsonify({'error': constants.NOT_JSON}), 400
        
    missing_fields = expected_fields_udpate - data.keys()
    if missing_fields:
        return jsonify({'error': constants.NOT_FIELDS, 'missing': list(missing_fields)}), 400

    updateMenu = service_manager.menu_service.update_person(data, get_jwt_identity())
    if updateMenu is constants.NOT_FOUND:
        return jsonify({'error': updateMenu + data['menuComercio']}), 404
    
    if updateMenu is None:
        return jsonify({'error': constants.INTERNAL_ERROR}), 500        
        
    return jsonify({'message': updateMenu}), 201