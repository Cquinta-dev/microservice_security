from flask_jwt_extended import create_access_token, create_refresh_token
from app.models.userModel import User
from datetime import datetime
from ..config import Config
from app.database import db
import bcrypt
import base64

class LoginService:

    def validate_login(self, data):

        user = User.query.filter_by(user=data['usuario']).first()
        if user:
            if user.password is None or not isinstance(user.password, str):
                return 500
            
            hashed_password_bytes = base64.b64decode(user.password)
            password_is_correct = bcrypt.checkpw(data['contrasenia'].encode('utf-8'), hashed_password_bytes)

            if password_is_correct:  
                if user.status_usr == 'E':
                    access_token = create_access_token(identity=user.user)
                    access_expiration = datetime.now() + Config.JWT_ACCESS_TOKEN_EXPIRES
                    if user.tocken_refresh is None:
                        refresh_token = create_refresh_token(identity=user.user)
                        user.tocken = refresh_token
                        refresh_expiration = datetime.now() + Config.JWT_REFRESH_TOKEN_EXPIRES
                        user.tocken_refresh = refresh_expiration
                    else:                        
                        if user.tocken_refresh > datetime.now():
                            refresh_token = user.tocken
                        else:
                            refresh_token = create_refresh_token(identity=user.user)
                            user.tocken = refresh_token
                            refresh_expiration = datetime.now() + Config.JWT_REFRESH_TOKEN_EXPIRES
                            user.tocken_refresh = refresh_expiration

                    accessSusses = {
                        'access_token': access_token,
                        'access_expiration': access_expiration,
                        'refresh_token': refresh_token
                    }

                    user.status_session = 'A'                    
                    user.open_session = datetime.now()
                    db.session.commit()

                    return accessSusses
                
                else:
                    return 402   
            else:
                return 401
        else:
            return None
        

    def refresh_token(self, usr):

        user = User.query.filter_by(user=usr).first()
        if user:
            if user.status_session == 'A':
                access_token = create_access_token(identity=usr)
                access_expiration = datetime.now() + Config.JWT_ACCESS_TOKEN_EXPIRES

                newAccess = {
                    "access_token": access_token,
                    "access_expires": access_expiration
                }

                return newAccess
            
            else :
                return {'Error':'La sessión fue finalizada.'}
        else:
            return None    
    
    
    def logout(self, usr):

        user = User.query.filter_by(user=usr).first()
        if user:
            if user.status_session == 'I' :
                return {'Exitoso':'la sesión ya finalizada.'}
            else:    
                user.status_session = 'I'        
                user.close_session = datetime.now()
                db.session.commit()

                return {'Exitoso':'Sesión Finalizada.'}
        else :
            return 404


    def reset_password(self, data):

        user = User.query.filter_by(user=data['usuario']).first()
        if user:
            if data['contrasenia']:
                password_hash = bcrypt.hashpw(data['contrasenia'].encode('utf-8'), bcrypt.gensalt())
                hashed_password_base64 = base64.b64encode(password_hash).decode('utf-8')
                user.password = hashed_password_base64

                db.session.commit()

            return user
        else:
            return None
        