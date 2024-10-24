from ..database import db

class AccessControl(db.Model):

    __tablename__ = 'accesscontrol'
    __table_args__ = {'schema': 'ap_security'}

    idAccess = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idModuleOption = db.Column(db.Integer, db.ForeignKey('ap_security.moduleoptions.idModuleOption'), nullable=False)
    idAction = db.Column(db.Integer, db.ForeignKey('ap_security.actions.idAction'), nullable=False)
    idRole = db.Column(db.Integer, db.ForeignKey('ap_security.roles.idRole'), nullable=False)

    #columnas de auditoria.
    status = db.Column(db.String(1), nullable=False)
    usr_create = db.Column(db.String(20), nullable=False)
    tim_create = db.Column(db.DateTime, nullable=False)  
    usr_update = db.Column(db.String(20))
    tim_update = db.Column(db.DateTime)    