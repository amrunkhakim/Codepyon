import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+mysqlconnector://your_username:your_password@localhost/my_database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
