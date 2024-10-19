from ..database import db

class User(db.Model):

    __tablename__ = 'users'
    __table_args__ = {'schema': 'ap_security'}
    
    id_person = db.Column(db.String(50), db.ForeignKey('ap_general.persons.id_person'), nullable=False)
    user = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(128), nullable=False)    
    status_session = db.Column(db.String(1), nullable=False)
    open_session = db.Column(db.DateTime)
    close_session = db.Column(db.DateTime)
    tocken_refresh = db.Column(db.DateTime)
    tocken = db.Column(db.String(500))
    
    #columnas de auditoria.
    status_usr = db.Column(db.String(1), nullable=False)
    usr_create = db.Column(db.String(20), nullable=False)
    tim_create = db.Column(db.DateTime, nullable=False)  
    usr_update = db.Column(db.String(20))
    tim_update = db.Column(db.DateTime)