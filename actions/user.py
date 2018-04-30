# -*- coding: utf-8 -*-
from app import db
from models.user import User


def save_user(user_dict):
    uid = user_dict.pop('id', None)
    if uid:
        user = User.query.filter_by(user_id=uid).first()
        user.username = user_dict['username']
        user.password = user_dict['password']
        user.email = user_dict['email']
    else:
        user = User(**user_dict)
    db.session.add(user)
    db.session.commit()
    return user


def delete_user(uid):
    user = User.query.filter_by(user_id=uid).first()
    db.session.delete(user)
    db.session.commit()
