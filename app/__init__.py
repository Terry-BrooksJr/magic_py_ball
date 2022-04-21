import psycopg2
import redis
from config import Config
from flask import Flask
from flask import current_app as app
from psycopg2 import connection, cursor
from flask_sqlalchemy import SQLAlchemy
from flask-redis import redis
import os

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
r =redis
