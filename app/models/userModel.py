from database import db
from datetime import datetime

class User(db.Model):

    __tablename__ = 'users'
    __table_args__ = {'schema': 'ejercicios'}
    
    user = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(128), nullable=False)
    id_person = db.Column(db.String(50), db.Foreingnkey('persons.id'), nullable=False)

    #columnas de auditoria.
    usr_create =  db.Column(db.String(20), nullable=False)
    tim_create =  db.Column(db.DateTime, nullable=False)  
    usr_update =  db.Column(db.String(20))
    tim_update =  db.Column(db.DateTime)
