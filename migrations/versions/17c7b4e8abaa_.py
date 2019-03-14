"""empty message

Revision ID: 17c7b4e8abaa
Revises: 60d3a9067ff8
Create Date: 2019-03-14 16:31:20.295359

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '17c7b4e8abaa'
down_revision = '60d3a9067ff8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
                    sa.Column('id', mysql.INTEGER(display_width=11),
                              autoincrement=True, nullable=False),
                    sa.Column('name', mysql.VARCHAR(
                        length=100), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    mysql_default_charset='utf8',
                    mysql_engine='InnoDB'
                    )
    op.create_table('users',
                    sa.Column('id', mysql.INTEGER(display_width=11),
                              autoincrement=True, nullable=False),
                    sa.Column('is_active', mysql.BOOLEAN(
                        display_width=1), autoincrement=False, nullable=True),
                    sa.Column('email', mysql.VARCHAR(
                        length=255), nullable=True),
                    sa.Column('email_confirmed_at',
                              mysql.TIMESTAMP(), nullable=True),
                    sa.Column('username', mysql.VARCHAR(
                        length=200), nullable=True),
                    sa.Column('password', mysql.VARCHAR(
                        length=260), nullable=True),
                    sa.Column('first_name', mysql.VARCHAR(
                        length=120), nullable=True),
                    sa.Column('last_name', mysql.VARCHAR(
                        length=120), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    mysql_default_charset='utf8',
                    mysql_engine='InnoDB'
                    )
    op.create_table('user_roles',
                    sa.Column('id', mysql.INTEGER(display_width=11),
                              autoincrement=True, nullable=False),
                    sa.Column('user_id', mysql.INTEGER(display_width=11),
                              autoincrement=False, nullable=True),
                    sa.Column('role_id', mysql.INTEGER(display_width=11),
                              autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    mysql_default_charset='utf8',
                    mysql_engine='InnoDB'
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_roles')
    op.drop_table('users')
    op.drop_table('roles')
    # ### end Alembic commands ###
