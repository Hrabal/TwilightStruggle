# -*- coding: utf-8 -*-
import locale
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import logging
logger = logging.getLogger('log_prod')
logger.setLevel(logging.DEBUG)
locale.setlocale(locale.LC_TIME, locale.getlocale())

app = Flask(__name__)
app.config.from_object('config')
login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)

if app.config.get('FLASKS3_ACTIVE'):
    from flask_s3 import FlaskS3, url_for
    s3 = FlaskS3(app)
    url_for = url_for
else:
    from flask import url_for
    url_for = url_for


logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

import controllers
