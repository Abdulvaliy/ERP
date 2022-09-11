import os
DEBUG = True


class Config:
    SECRET_KEY = "MyTopSecretKey"  # os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///erp.db'  # os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_PERMANENT = False
    SESSION_TYPE = 'filesystem'

