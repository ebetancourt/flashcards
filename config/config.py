import os

DEBUG = True
SECRET_KEY = 'REPLACE ME - this value is here as a placeholder.'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False
