from app.models.userModel import User
from app.models.personModel import Person
from app.database import db
from datetime import datetime
import bcrypt
import base64

class UserService:

    def create_user(self, data, usr):

        getPerson = Person.query.filter_by(id_person=data['personId']).first()
        if getPerson:
            password_hash = bcrypt.hashpw(data['contrasenia'].encode('utf-8'), bcrypt.gensalt())
            hashed_password_base64 = base64.b64encode(password_hash).decode('utf-8')
            new_user = User(
                id_person = data['personId'],
                user = data['usuario'],
                password = hashed_password_base64,
                status_session = 'I',
                status_usr = 'E',
                usr_create = usr,
                tim_create = datetime.now()
            )

            db.session.add(new_user)
            db.session.commit()

            return new_user
        
        else:

            return None
        

    def get_user(self, id):

        user = User.query.filter_by(user=id).first()
        if user:
            data = {
                'personId': user.id_person,
                'usuario': user.user,
                'estado': user.status_usr
            }

            return data

        else:

            return None
        
        
    def update_user(self, data, usr):

        user = User.query.filter_by(user=data['usuario']).first()
        if user:        
            if data['estado']:
                user.status_usr = data['estado']

            user.usr_update = usr
            user.tim_update = datetime.now()
            db.session.commit()

            return user

        else:

            return None