from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from flask_user import UserMixin

from models.Base import Base
from app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    active = Column('is_active', Boolean(),
                    nullable=False, server_default='1')
    username = Column(String(255),
                      nullable=False, unique=True)
    password = Column(String(255), nullable=False, server_default='')
    # Define the relationship to Role via UserRoles
    # roles = relationship('Role', secondary='user_roles')


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer(), primary_key=True)
    name = Column(String(50), unique=True)


class UserRoles(Base):
    __tablename__ = 'user_roles'
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey(
        'users.id', ondelete='CASCADE'))
    role_id = Column(Integer(), ForeignKey(
        'roles.id', ondelete='CASCADE'))
