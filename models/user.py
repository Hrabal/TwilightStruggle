# -*- coding: utf-8 -*-
from sqlalchemy.orm import relationship
from passlib.hash import bcrypt

from app import db
from models.dbtools import Dictable
from models.game import GamePlayers


class User(db.Model, Dictable):
    user_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    username = db.Column(db.String(64),
                         index=True,
                         unique=True,
                         nullable=False)
    password_hash = db.Column(db.String(300),
                              nullable=False)
    email = db.Column(db.String(300))
    pic = db.Column(db.String(64), default='anonymous.jpg')
    country = db.Column(db.String(2))
    birth = db.Column(db.Date())
    tagline = db.Column(db.String(255))
    joined = db.Column(db.Date())
    level = db.Column(db.Integer(), default=1)
    games = relationship('GamePlayers', backref='player', primaryjoin=user_id == GamePlayers.user_id)

    def __init__(self, username, password, email):
        self.username = username
        self.password_hash = bcrypt.encrypt(password)
        self.email = email

    def validate_password(self, password):
        return bcrypt.verify(password, self.password_hash)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.user_id)

    def __repr__(self):
        return '<User %r>' % (self.username)
