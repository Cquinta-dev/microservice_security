from sqlalchemy import exists
from ..models.company_model import  Company
from ..models.menu_model import Menu
from ..database import db 
from .constants import constants


class ValidatorOrm:


    def validate_company_status(id):
        search_company = Company.query.filter_by(idCompany=id).first()
        if search_company: 
            if search_company.status == constants.ENABLED:            
                return constants.Ok
            
            return f"Company {search_company.nameCompany} {constants.MESSAGE_DISABLED}" 

        return f"{constants.NOT_EXIST} Company {id}"


    def menu_exists(idCompany):
            return db.session.query(exists().where(Menu.idCompany == idCompany)).scalar()
    
    
    def validate_menu_status(id):
        search_menu = Menu.query.filter_by(idMenu=id).first()
        if search_menu: 
            if search_menu.status == constants.ENABLED:            
                return constants.Ok
            
            return f"Company {search_menu.nameMenu} {constants.MESSAGE_DISABLED}" 

        return f"{constants.NOT_EXIST} Company {id}"
        
