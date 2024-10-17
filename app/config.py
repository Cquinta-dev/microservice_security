import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://pythoapp:Manager1@localhost:5432/prototipo')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret')  # Cambia esto en producción