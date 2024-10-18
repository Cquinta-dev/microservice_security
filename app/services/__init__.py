from .person_service import PersonService
from .user_service import UserService

class ServiceManager:
    def __init__(self):
        self.person_service = PersonService()
        self.user_service = UserService()

service_manager = ServiceManager()