import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    SECRET_KEY = os.urandom(32)

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:!QAYxsw2@192.168.178.100:5432/fyyur'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
