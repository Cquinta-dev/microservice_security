from .user_service import UserService
from .login_service import LoginService
from .menu_service import MenuService

class ServiceManager:
    
    def __init__(self):
        self.user_service = UserService()
        self.login_service = LoginService()
        self.menu_service = MenuService()

service_manager = ServiceManager()