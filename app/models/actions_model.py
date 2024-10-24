from ..database import db

class Actions(db.Model):

    __tablename__ = 'actions'
    __table_args__ = {'schema': 'ap_security'}

    idAction = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nameAction = db.Column(db.String(100), nullable=False, unique=True)

    #columnas de auditoria.
    status = db.Column(db.String(1), nullable=False)
    usr_create = db.Column(db.String(20), nullable=False)
    tim_create = db.Column(db.DateTime, nullable=False)  
    usr_update = db.Column(db.String(20))
    tim_update = db.Column(db.DateTime)