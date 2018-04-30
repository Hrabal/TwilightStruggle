# -*- coding: utf-8 -*-
from sqlalchemy.orm import relationship

from app import db
from models.dbtools import Dictable


class GamePlayers(db.Model):
    __tablename__ = 'game_players'
    game_id = db.Column(db.Integer, db.ForeignKey('game.game_id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    joined_game = db.Column(db.DateTime)
    score = db.Column(db.Integer)


class Game(db.Model, Dictable):
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    link = db.Column(db.String(300), nullable=False)
    active = db.Column(db.Boolean(), nullable=False, default=True)
    order = db.Column(db.Float(), nullable=False, default=0)
    menu = db.Column(db.String(10), default='MAIN')
    players = relationship('GamePlayers', backref='game', primaryjoin=game_id == GamePlayers.game_id)
    ended = db.Column(db.Boolean(), nullable=False, default=False)
