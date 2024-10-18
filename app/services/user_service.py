from app.models.userModel import User
from app.models.personModel import Person
from app.database import db
from datetime import datetime

class UserService:

    def create_user(self, data):
        
        getPerson = Person.query.filter_by(id_person=data['personId']).first()
        if getPerson:
            new_user = User(
                id_person = data['personId'],
                user = data['usuario'],
                password = data['contrasenia'],
                status_session = 'D',
                usr_create=data['uCreacion'],
                tim_create=datetime.now()
            )

            db.session.add(new_user)
            db.session.commit()

            return new_user
        
        else:

            return None