"""empty message

Revision ID: 52ef24ec7f77
Revises: 93d793e9cb74
Create Date: 2019-03-18 18:21:48.013341

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '52ef24ec7f77'
down_revision = '93d793e9cb74'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('cards', sa.Column(
        'user', mysql.INTEGER(display_width=11), nullable=True))


def downgrade():
    op.drop_column('cards', 'user')
