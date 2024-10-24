from ..utils.validator_orm import ValidatorOrm
from ..models.menu_model import Menu
from ..utils.constants import constants
from ..database import db 
from datetime import datetime

class MenuService:


    def create_menu(self, data, usr):
        try:
            if ValidatorOrm.menu_exists(data['codComercio']):
                return f"{constants.EXIST}{data['menuComercio']}"
            else:
                validation = ValidatorOrm.validate_company_status(data['codComercio'])
                if validation == constants.Ok:
                    new_menu = Menu (
                        idCompany = data['codComercio'],
                        nameMenu = data['menuComercio'],

                        status = constants.ENABLED,
                        usr_create = usr,
                        tim_create = datetime.now()
                    )
                    
                    db.session.add(new_menu)
                    db.session.commit()

                    return f"{constants.CREATE}Menu {data['menuComercio']}"
                else:
                    return validation
               
        except Exception as e:
            print('---------------> ERROR create_menu: ---------------> ', e)
            return None
    

    def get_departaments(self):
        read_menus = Menu.query.all()
        if read_menus:
            data = {
                'menus': [
                    {
                        'id': p.idMenu,
                        'codComercio': p.idCompany,
                        'menuComercio': p.nameMenu,                    
                        'estadoMenu': p.status,
                        'usrIngreso': p.usr_create,
                        'detIngreso': p.tim_create,
                        'usrModifico': p.usr_update,
                        'detModifico': p.tim_update
                    } for p in read_menus
                ]
            }
        else:
            return None

        return data


    def get_combo_menu(self, id):
        read_menus = Menu.query.filter(
                                Menu.idCompany == id,
                                Menu.status == constants.ENABLED)
        if read_menus.count() == 0:
            return None
        
        if read_menus:
            data = {
                'menu': [
                    {
                        'id': p.idMenu,
                        'departamento': p.nameMenu
                    } for p in read_menus
                ]
            }
        
        return data


    def update_person(self, data, usr):
        try:        
            refresh_menu = Menu.query.filter_by(idMenu=data['id']).first()
            if refresh_menu:
                validation = ValidatorOrm.validate_company_status(data['codComercio']) 
                if validation == constants.Ok:
                    if data['codComercio']: 
                        refresh_menu.idCompany = data['codComercio']

                    if data['menuComercio']: 
                        refresh_menu.nameMenu = data['menuComercio']

                    if data['estadoMenu']:
                        refresh_menu.status = data['estadoMenu']

                    refresh_menu.usr_update = usr
                    refresh_menu.tim_update = datetime.now()            
                    db.session.commit()

                    return f"{constants.UPDATE}Menu {data['menuComercio']}"
                else:
                    return validation
        
            return constants.NOT_FOUND

        except Exception as e:
            print('---------------> ERROR update_menu: ---------------> ', e)
            return None