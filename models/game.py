# -*- coding: utf-8 -*-
from sqlalchemy.orm import relationship

from app import db
from models.dbtools import Dictable


class GamePlayers(db.Model):
    __tablename__ = 'game_players'
    game_id = db.Column(db.Integer, db.ForeignKey('game.game_id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    score = db.Column(db.Integer)
    space = db.Column(db.Integer)
    faction = db.Column(db.String(2))


class Game(db.Model, Dictable):
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    started = db.Column(db.DateTime)
    ended = db.Column(db.DateTime)
    players = relationship('GamePlayers', backref='game', primaryjoin=game_id == GamePlayers.game_id)
    turn = db.Column(db.Integer)
    round = db.Column(db.Integer)
    defcon = db.Column(db.Integer)
    req_ops = db.Column(db.Integer)
