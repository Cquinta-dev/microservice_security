from ..database import db

class RoleUser(db.Model):

    __tablename__ = 'roleuser'
    __table_args__ = {'schema': 'ap_security'}

    idRoleUser = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idRole = db.Column(db.Integer, db.ForeignKey('ap_security.roles.idRole'), nullable=False)
    idUser = db.Column(db.Integer, db.ForeignKey('ap_security.users.idUser'), nullable=False)

    #columnas de auditoria.
    status = db.Column(db.String(1), nullable=False)
    usr_create = db.Column(db.String(20), nullable=False)
    tim_create = db.Column(db.DateTime, nullable=False)  
    usr_update = db.Column(db.String(20))
    tim_update = db.Column(db.DateTime)