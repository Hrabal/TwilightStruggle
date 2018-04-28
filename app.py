# -*- coding: utf-8 -*-
import locale

from flask import Flask
from flask_s3 import FlaskS3
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

s3 = FlaskS3(app)

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

import models
import controllers
