#from ..models.person_model import Person
from ..models.users_model import Users
from ..database import db
from datetime import datetime
import bcrypt
import base64

class UserService:

    def create_user(self, data, usr):

        #getPerson = Person.query.filter_by(id_person=data['personId']).first()
        #if getPerson:
            #if getPerson.status_per == 'E':
                password_hash = bcrypt.hashpw(data['contrasenia'].encode('utf-8'), bcrypt.gensalt())
                hashed_password_base64 = base64.b64encode(password_hash).decode('utf-8')
                new_user = Users(
                    id_person = data['personId'],
                    idUser = data['usuario'],
                    password = hashed_password_base64,
                    status_session = 'I',
                    status_usr = 'E',
                    usr_create = usr,
                    tim_create = datetime.now()
                )

                db.session.add(new_user)
                db.session.commit()
                
                return new_user
            #else:
            #    return {'message': 'Person status inactive'}
        #else:
        #    return None
        

    def get_user(self, id):

        user = Users.query.filter_by(idUser=id).first()
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

        user = Users.query.filter_by(idUser=data['usuario']).first()
        if user:        
            if data['estado']:
                user.status_usr = data['estado']

            user.usr_update = usr
            user.tim_update = datetime.now()
            db.session.commit()

            return user
        else:
            return None