from flask import Blueprint
from .user_routes import user_routes
from .login_routes import login_routes

main_routes = Blueprint('main', __name__)

# Registra los blueprints
main_routes.register_blueprint(user_routes)
main_routes.register_blueprint(login_routes)

@main_routes.route('/')
def index():
    return {"message": "Welcome to the API!"}