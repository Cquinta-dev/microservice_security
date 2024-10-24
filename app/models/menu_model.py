from ..database import db

class Menu(db.Model):

    __tablename__ = 'menu'
    __table_args__ = {'schema':'ap_security'}

    idMenu = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idCompany = db.Column(db.Integer, db.ForeignKey('ap_general.company.idCompany'), nullable=False)
    nameMenu = db.Column(db.String(100), nullable=False, unique=True)

    #columnas de auditoria.
    status = db.Column(db.String(1), nullable=False)
    usr_create = db.Column(db.String(20), nullable=False)
    tim_create = db.Column(db.DateTime, nullable=False)  
    usr_update = db.Column(db.String(20))
    tim_update = db.Column(db.DateTime)