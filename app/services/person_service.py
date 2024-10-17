from app.models.personModel import Person
from app.database import db

class PersonService:
    def create_person(self, data):

        new_person = Person(
        id_person=data['id_person'], 
        name=data['name'],
        lastname=data['lastname'],
        email=data['email'],
        usr_create=data['create'],
        tim_create=data['dayCreate'])
        
        db.session.add(new_person)
        db.session.commit()

        return new_person