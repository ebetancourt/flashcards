import os
from flask import Flask

from blueprints.userspace import userspace_blueprint
from blueprints.admin import admin_blueprint

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.config')

app.secret_key = app.config.get('SECRET_KEY')

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

app.register_blueprint(userspace_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')

if __name__ == '__main__':
    app.run()
