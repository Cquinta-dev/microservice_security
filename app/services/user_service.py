from app.models.userModel import User
from app.database import db
from datetime import datetime

class UserService:
    def create_user(self, data):

        new_user = User(
        id_person = data.id_person,
        user = data.user,
        password = data.password,
        usr_create=data['create'],
        tim_create=datetime.now())

        db.session.add(new_user)
        db.session.commit()

        return new_user