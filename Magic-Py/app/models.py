from flask_appbuilder import Model  
from flask_appbuilder.models.mixins import AuditMixin
from sqlalchemy import Column,Text, Integer, DateTime

class Wisdom(Model,AuditMixin):
    __tablename__ = "Wisdom Vault"
    wisdom_id = Column(Integer(primary_key=True, index=True, unique=True))
    answer = Column(Text())
    date_added = Column(DateTime(index=True))
    def __init__(self, wisdom_id, answer, date_added):
        self.wisdom_id = wisdom_id
        self.answer = answer
        self._date_added = date_added

    def __repr__(self):
        return f'Wisdom Id {self.wisdom_id} states {self.answer} and was added on {self.date_added}'
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
