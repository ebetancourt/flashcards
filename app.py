import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_user import UserManager, current_user

from blueprints.userspace import userspace_blueprint
from blueprints.admin import admin_blueprint
from models.User import User, Role, UserRoles

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.config')

app.secret_key = app.config.get('SECRET_KEY')

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

db = SQLAlchemy(app)

user_manager = UserManager(app, db, User)

migrate = Migrate(app, db)

app.register_blueprint(userspace_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')

if __name__ == '__main__':
    app.run()
