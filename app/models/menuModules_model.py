from ..database import db

class MenuModules(db.Model):

    __tablename__ = 'menumodules'
    __table_args__ = {'schema': 'ap_security'}

    idMenuModule = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idMenu = db.Column(db.Integer, db.ForeignKey('ap_security.menu.idMenu'), nullable=False)
    nameModule = db.Column(db.String(100), nullable=False, unique=True)

    #columnas de auditoria.
    status = db.Column(db.String(1), nullable=False)
    usr_create = db.Column(db.String(20), nullable=False)
    tim_create = db.Column(db.DateTime, nullable=False)  
    usr_update = db.Column(db.String(20))
    tim_update = db.Column(db.DateTime)