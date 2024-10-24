from ..database import db

class Roles(db.Model):

    __tablename__ = 'roles'
    __table_args__ = {'schema': 'ap_security'}

    idRole = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nameRole = db.Column(db.String(100), nullable=False, unique=True)

    #columnas de auditoria.
    status = db.Column(db.String(1), nullable=False)
    usr_create = db.Column(db.String(20), nullable=False)
    tim_create = db.Column(db.DateTime, nullable=False)  
    usr_update = db.Column(db.String(20))
    tim_update = db.Column(db.DateTime)