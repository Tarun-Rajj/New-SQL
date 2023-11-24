
# from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

from sqlalchemy.orm import DeclarativeBase,declarative_base
from sqlalchemy import Integer,Column,String,ForeignKey
from app import db

Base = declarative_base()
metadata = Base.metadata



class Base(DeclarativeBase):
    pass

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False) # It is used to identify which user have what role.
    role = db.relationship('Role', backref=db.backref('users', lazy=True))

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Pending')
    assigned_to = db.Column(db.String, db.ForeignKey('user.id'))
    assigned_by = db.Column(db.String, db.ForeignKey('user.id'))
    
    assigned_to_user = db.relationship('User', foreign_keys=[assigned_to], backref='tasks_assigned_to', lazy=True, primaryjoin="Task.assigned_to == User.id")
    assigned_by_user = db.relationship('User', foreign_keys=[assigned_by], backref='tasks_assigned_by', lazy=True, primaryjoin="Task.assigned_by == User.id")

