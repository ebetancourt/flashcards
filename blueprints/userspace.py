import flask
from flask_user import current_user, login_required, roles_required
from flask_login import logout_user
from models.Card import Card

userspace_blueprint = flask.Blueprint('userspace_blueprint', __name__)


@userspace_blueprint.route('/')
@login_required
def index():
    next_card = Card.get_next(current_user.id)
    return flask.render_template('cards.html', card=next_card, user=current_user)


@userspace_blueprint.route('/mark/<int:card_id>/right')
@login_required
def mark_right(card_id=None):
    if card_id is not None:
        card = Card.find_by_id(card_id)
        card.mark_right()
        card.save()
    return flask.redirect(flask.url_for('userspace_blueprint.index'))


@userspace_blueprint.route('/mark/<int:card_id>/wrong')
@login_required
def mark_wrong(card_id=None):
    if card_id is not None:
        card = Card.find_by_id(card_id)
        card.mark_wrong()
        card.save()
    return flask.redirect(flask.url_for('userspace_blueprint.index'))


@userspace_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return flask.redirect(flask.url_for('userspace_blueprint.index'))
