from abc import ABC, abstractmethod
from typing import List

from core.todo.ports import ITodoAccessor  # replace with your actual ITodoAccessor import
from core.todo.models import TodoDomain  # replace with your actual TodoDomain import
from infrastructure.todo.models import Todo  # replace with your actual Todo import
from core.common.utils import ObjectMapperUtil
from infrastructure.db import db

class TodoAccessor(ITodoAccessor):

    def create(self, title: str, description: str, priority: str, dueDate: str) -> TodoDomain:
        todo = Todo(title=title, description=description, priority=priority, dueDate=dueDate)
        db.session.add(todo)
        db.session.commit()
        return ObjectMapperUtil.map(todo, TodoDomain)

    def get_all(self) -> List[TodoDomain]:
        todos = Todo.query.all()
        return ObjectMapperUtil.map_array(todos, TodoDomain)

    def get_by_id(self, id: int) -> TodoDomain:
        todo = Todo.query.get(id)
        return ObjectMapperUtil.map(todo, TodoDomain)

    def update(self, id: int, title: str, description: str, priority: str, dueDate: str) -> TodoDomain:
        todo = Todo.query.get(id)
        todo.title = title
        todo.description = description
        todo.priority = priority
        todo.dueDate = dueDate
        db.session.commit()
        return ObjectMapperUtil.map(todo, TodoDomain)

    def delete(self, id: int) -> None:
        todo = Todo.query.get(id)
        db.session.delete(todo)
        db.session.commit()