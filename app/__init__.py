from flask import Flask
from .config import Config
from .database import db
from .routes import main_routes  # o person_routes si es específico

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()  # Crear tablas en la base de datos

    app.register_blueprint(main_routes)  # o app.register_blueprint(person_routes)

    return app