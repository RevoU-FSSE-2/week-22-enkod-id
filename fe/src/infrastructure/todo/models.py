from infrastructure.db import db
from enum import Enum
from sqlalchemy import Enum as EnumType
from datetime import datetime

class Priority(Enum):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    priority = db.Column(EnumType(Priority), default=Priority.LOW, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)

