import flask
from flask_user import current_user, login_required, roles_required

userspace_blueprint = flask.Blueprint('userspace_blueprint', __name__)


@userspace_blueprint.route('/')
@userspace_blueprint.route('/test')
@login_required
def index():
    return flask.render_template('cards.html', message='view your cards here')
