# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.getenv('SECRET_KEY')

# DB
RDS_TYP = os.getenv('RDS_TYP')
RDS_URL = os.getenv('RDS_URL')
RDS_DB = os.getenv('RDS_DB')
RDS_USR = os.getenv('RDS_USR')
RDS_PWD = os.getenv('RDS_PWD')
SQLALCHEMY_DATABASE_URI = f'{RDS_TYP}://{RDS_USR}:{RDS_PWD}@{RDS_URL}/{RDS_DB}'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# S3
FLASKS3_BUCKET_NAME = os.getenv('FLASKS3_BUCKET_NAME', None)
FLASKS3_ACTIVE = os.getenv('FLASKS3_ACTIVE', False) and FLASKS3_BUCKET_NAME
