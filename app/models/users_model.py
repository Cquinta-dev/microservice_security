from ..database import db

class Users(db.Model):

    __tablename__ = 'users'
    __table_args__ = {'schema':'ap_security'}    
    
    idUser = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idPerson = db.Column(db.Integer, db.ForeignKey('prototipo.ap_general.person.idPerson'), nullable=False)
    userName = db.Column(db.String(20), nullable=False, unique=True)    
    password = db.Column(db.String(128), nullable=False)    
    statusSession = db.Column(db.String(1), nullable=False)
    openSession = db.Column(db.DateTime)
    closeSession = db.Column(db.DateTime)
    validTimeTocken = db.Column(db.DateTime)
    tockenRefresh = db.Column(db.String(500))
    
    #columnas de auditoria.
    status = db.Column(db.String(1), nullable=False)
    usr_create = db.Column(db.String(20), nullable=False)
    tim_create = db.Column(db.DateTime, nullable=False)  
    usr_update = db.Column(db.String(20))
    tim_update = db.Column(db.DateTime)