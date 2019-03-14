import flask

userspace_blueprint = flask.Blueprint('userspace_blueprint', __name__)


@userspace_blueprint.route('/')
@userspace_blueprint.route('/test')
def index():
    return flask.render_template('cards.html', message='view your cards here')
