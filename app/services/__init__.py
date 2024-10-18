from .person_service import PersonService
from .user_service import UserService
from .login_service import LoginService

class ServiceManager:
    def __init__(self):
        self.person_service = PersonService()
        self.user_service = UserService()
        self.login_service = LoginService()

service_manager = ServiceManager()