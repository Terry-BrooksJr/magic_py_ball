from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text, DateTime
from app import db

# ? Possible SQL Execute Statement
# SELECT column FROM table
# ORDER BY RANDOM()
# LIMIT 1

class Wisdom():
    def __init__(self, wisdom_id, answer, date_added):
        self._wisdom_id = wisdom_id
        self.ansewer = answer
        self.date_added = date_added