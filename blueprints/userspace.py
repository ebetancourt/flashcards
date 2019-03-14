import flask

userspace_blueprint = flask.Blueprint('userspace_blueprint', __name__)


@userspace_blueprint.route('/')
@userspace_blueprint.route('/test')
def index():
    return 'view your cards here'
