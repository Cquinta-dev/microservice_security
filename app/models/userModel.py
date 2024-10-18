from ..database import db

class User(db.Model):

    __tablename__ = 'users'
    __table_args__ = {'schema': 'ejercicios'}
    
    id_person = db.Column(db.String(50), db.ForeignKey('ejercicios.persons.id_person'), nullable=False)
    user = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(128), nullable=False)    
    status_session = db.Column(db.String(1), nullable=False)
    tim_tocken_access =  db.Column(db.DateTime)
    tocken_access = db.Column(db.String(255))
    tim_tocken_refresh =  db.Column(db.DateTime)
    tocken_refresh = db.Column(db.String(255))

    #columnas de auditoria.
    status_usr = db.Column(db.String(1))
    usr_create = db.Column(db.String(20), nullable=False)
    tim_create = db.Column(db.DateTime, nullable=False)  
    usr_update = db.Column(db.String(20))
    tim_update = db.Column(db.DateTime)