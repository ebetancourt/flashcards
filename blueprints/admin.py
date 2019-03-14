import flask

admin_blueprint = flask.Blueprint('admin_blueprint', __name__)


@admin_blueprint.route('/')
@admin_blueprint.route('/test')
def index():
    return 'admin area. Edit cards here'
