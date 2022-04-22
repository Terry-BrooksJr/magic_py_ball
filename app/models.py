from enum import unique
from flask_sqlalchemy import SQLAlchemy
from flask import current_app as app 
# from sqlalchemy import Integer, String, Text, DateTime, Column
from app import db
from psycopg2 import connection, cursor

# ? Possible SQL Execute Statement
# SELECT column FROM table
# ORDER BY RANDOM()
# LIMIT 1

class Wisdom(db.Model):
    __tablename__ = "Wisdom Vault"
    wisdom_id = db.Column(db.Interger(primary_key=True, index=True, unique=True))
    answer = db.Column(db.Text())
    date_added = db.Column(db.DateTime(index=True))
    def __init__(self, wisdom_id, answer, date_added):
        self.wisdom_id = wisdom_id
        self.answer = answer
        self._date_added = date_added

    def __repr__(self):
        return f'Wisdom Id {self.wisdom_id} states {self.answer} and was added on {self.date_added} ' 