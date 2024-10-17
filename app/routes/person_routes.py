from flask import Blueprint, jsonify, request
from app.services import service_manager
from ..schemas.person_schema import expected_fields_create
from ..schemas.person_schema import expected_fields_update

person_routes = Blueprint('person', __name__)

#Method for create person.
@person_routes.route('/createPerson',methods=['POST'])
def create_person():
    try:
        data = request.get_json(force=True)

        if data is None:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        missing_fields = expected_fields_create - data.keys()
        if missing_fields:
            return jsonify({'error': 'Missing fields', 'missing': list(missing_fields)}), 400
        
        service_manager.person_service.create_person(data)
        
        return jsonify({'message': 'Person created'}), 201
    
    except Exception as e:

        return jsonify({'error': 'Internal Server'}), 500    


#Method for get list to person.
@person_routes.route('/allPersons', methods=['GET'])
def get_persons():

    persons = service_manager.person_service.get_all_persons()
    if persons is None:
        return jsonify({'error':'Not data found'}), 404

    return jsonify(persons), 200


#Method for get one person.
@person_routes.route('/getPerson', methods=['GET'])
def get_person():
    personID = request.args.get('id')

    if personID: 
        person = service_manager.person_service.get_person(personID)
        if person:
            return jsonify(person), 200
        
        return jsonify({'error':'Not data found'}), 404

    return jsonify({'error': 'Id was not provided'}), 400


#Method for udpate person.
@person_routes.route('/updatePerson', methods=['PUT'])
def update_person():    
    try:
        personID = request.args.get('id')
        data = request.get_json(force=True)

        if personID: 
            if data is None:
                return jsonify({'error': 'No JSON data provided'}), 400
            
            missing_fields = expected_fields_update - data.keys()
            if missing_fields:
                return jsonify({'error': 'Missing fields', 'missing': list(missing_fields)}), 400

            updatePerson = service_manager.person_service.update_person(personID, data)
            if updatePerson is None:
                return jsonify({'error':'Not data found'}), 404
            
            return jsonify({'message': 'Person updated'}), 201

        return jsonify({'error': 'Id was not provided'}), 400

    except Exception as e:

            return jsonify({'error': 'Internal Server'}), 500    
