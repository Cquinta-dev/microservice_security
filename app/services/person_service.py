from app.models.personModel import Person
from app.database import db
from datetime import datetime

class PersonService:


    def create_person(self, data):

        new_person = Person (
            id_person = data['id'], 
            name = data['nombres'],
            lastname = data['apellidos'],
            email = data['correo'],
            usr_create = data['uCreacion'],
            tim_create = datetime.now()
        )
        
        db.session.add(new_person)
        db.session.commit()

        return new_person

    
    def get_all_persons(self):

        getPersons = Person.query.all()
        data = {
            'personas': [
                {
                    'id': p.id_person,
                    'nombres': p.name,
                    'apellidos': p.lastname,
                    'correo': p.email
                } for p in getPersons
            ]
        }

        return data
    

    def get_person(self, id):

        getPerson = Person.query.filter_by(id_person=id)
        data = {
            'personas': [
                {
                    'id': p.id_person,
                    'nombres': p.name,
                    'apellidos': p.lastname,
                    'correo': p.email
                } for p in getPerson
            ]
        }

        return data


    def update_person(self, id, data):
        
        person = Person.query.filter_by(id_person=id).first()
        if person:            
            if data['nombres']: 
                person.name = data['nombres']
            
            if data['apellidos']:
                person.lastname = data['apellidos']
            
            if data['correo']:
                person.email = data['correo']

            person.usr_update = data['uActualiza']
            person.tim_update = datetime.now()            
            db.session.commit()

            return person
        
        return None