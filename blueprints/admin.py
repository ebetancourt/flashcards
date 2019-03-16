import flask
from flask import request
from models.Card import Card
from flask_user import current_user, login_required, roles_required

admin_blueprint = flask.Blueprint('admin_blueprint', __name__)


@admin_blueprint.route('/')
@admin_blueprint.route('/test')
@login_required
def index():
    return 'admin area. Edit cards here'


@admin_blueprint.route('/new')
@login_required
def create_card():
    return flask.render_template('admin/card_form.html', card=Card())


@admin_blueprint.route('/save', methods=['POST'])
@login_required
def save_card():
    if request.method == 'POST':
        if 'id' in request.form:
            card = Card.find(request.form['id'])
        else:
            card = Card()

        card.word = request.form['word']
        card.definition = request.form['definition']
        card.save()

    return flask.render_template('admin/card_form.html', card=card)
