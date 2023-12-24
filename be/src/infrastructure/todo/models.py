from core.todo.constants import TodoPriority  # replace with your actual TodoPriority import
from infrastructure.db import db
from enum import Enum
from sqlalchemy import Enum as EnumType

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    priority = db.Column(EnumType(TodoPriority), default=TodoPriority.LOW, nullable=False)
    dueDate = db.Column(db.DateTime, nullable=False)