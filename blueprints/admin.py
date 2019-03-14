import flask
from flask_user import current_user, login_required, roles_required

admin_blueprint = flask.Blueprint('admin_blueprint', __name__)


@admin_blueprint.route('/')
@admin_blueprint.route('/test')
@login_required
def index():
    return 'admin area. Edit cards here'
