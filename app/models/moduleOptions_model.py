from ..database import db

class ModuleOptions(db.Model):

    __tablename__ = 'moduleoptions'
    __table_args__ = {'schema': 'ap_security'}

    idModuleOption = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idMenu = db.Column(db.Integer, db.ForeignKey('ap_security.menu.idMenu'), nullable=False)
    idMenuModule = db.Column(db.Integer, db.ForeignKey('ap_security.menumodules.idMenuModule'), nullable=False)
    nameOption = db.Column(db.String(100), nullable=False, unique=True)
    icon = db.Column(db.String(50), nullable=False)
    endPoint = db.Column(db.String(100), nullable=False, unique=True)

    #columnas de auditoria.
    status = db.Column(db.String(1), nullable=False)
    usr_create = db.Column(db.String(20), nullable=False)
    tim_create = db.Column(db.DateTime, nullable=False)  
    usr_update = db.Column(db.String(20))
    tim_update = db.Column(db.DateTime)