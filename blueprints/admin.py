import flask
from flask import request, current_app, url_for
from models.Card import Card
from flask_user import current_user, login_required, roles_required

admin_blueprint = flask.Blueprint('admin_blueprint', __name__)


@admin_blueprint.route('/')
@admin_blueprint.route('/test')
@login_required
def index():
    user_cards = Card.all_for_current_user(current_user.id)
    return flask.render_template('admin/card_list.html', cards=user_cards)


@admin_blueprint.route('/new')
@admin_blueprint.route('/edit/<int:card_id>')
@login_required
def card_form(card_id=None):
    if card_id is None:
        card = Card()
    else:
        card = Card.find_by_id(card_id)
    return flask.render_template('admin/card_form.html', card=card)


@admin_blueprint.route('/save', methods=['POST'])
@login_required
def save_card():
    if request.method == 'POST':
        if 'id' in request.form:
            card = Card.find_by_id(request.form['id'])
        else:
            card = Card()
            card.user = current_user.id

        card.word = request.form['word']
        card.definition = request.form['definition']
        card.save()

    return flask.redirect(url_for('admin_blueprint.card_form', card_id=card.id))
