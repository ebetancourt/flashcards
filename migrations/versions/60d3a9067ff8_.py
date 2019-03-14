"""empty message

Revision ID: 60d3a9067ff8
Revises: 
Create Date: 2019-03-14 13:01:56.110802

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '60d3a9067ff8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cards',
                    sa.Column('id', mysql.INTEGER(
                        display_width=11, unsigned=True), autoincrement=True, nullable=False),
                    sa.Column('word', mysql.VARCHAR(
                        length=250), nullable=True),
                    sa.Column('definition', mysql.TEXT(), nullable=True),
                    sa.Column('wrong_count', mysql.INTEGER(display_width=11),
                              autoincrement=False, nullable=True),
                    sa.Column('available', mysql.DATETIME(), nullable=True),
                    sa.Column('bucket', mysql.INTEGER(display_width=11),
                              autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    mysql_default_charset='utf8',
                    mysql_engine='InnoDB'
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cards')
    # ### end Alembic commands ###
