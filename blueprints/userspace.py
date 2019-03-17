import flask
from flask_user import current_user, login_required, roles_required
from models.Card import Card

userspace_blueprint = flask.Blueprint('userspace_blueprint', __name__)


@userspace_blueprint.route('/')
@userspace_blueprint.route('/test')
@login_required
def index():
    next_card = Card.get_next()
    return flask.render_template('cards.html', card=next_card)
