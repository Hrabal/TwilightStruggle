# -*- coding: utf-8 -*-
from app import db
from models.dbtools import Dictable


class Menu(db.Model, Dictable):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    link = db.Column(db.String(300), nullable=False)
    active = db.Column(db.Boolean(), nullable=False, default=True)
    order = db.Column(db.Float(), nullable=False, default=0)
    menu = db.Column(db.String(10), default='MAIN')


class Content(db.Model, Dictable):
    content_id = db.Column(db.Integer,
                           primary_key=True,
                           autoincrement=True)
    title = db.Column(db.String(255), nullable=True)
    text = db.Column(db.Text())
