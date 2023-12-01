from abc import ABC, abstractmethod
from typing import List

from core.todo.ports import ITodoAccessor
from core.todo.models import TodoDomain
from infrastructure.todo.models import Todo
from core.common.utils import ObjectMapperUtil
from infrastructure.db import db

class TodoAccessor(ITodoAccessor):

    def create(self, title: str, description: str, priority: str, due_date: datetime) -> TodoDomain:
        todo = Todo(title=title, description=description, priority=priority, due_date=due_date)
        db.session.add(todo)
        db.session.commit()
        return ObjectMapperUtil.map(todo, TodoDomain)

    def get_all(self) -> List[TodoDomain]:
        todos = Todo.query.all()
        return ObjectMapperUtil.map_array(todos, TodoDomain)

    def get_by_id(self, todo_id: int) -> TodoDomain:
        todo = Todo.query.get(todo_id)
        return ObjectMapperUtil.map(todo, TodoDomain)

    def update(self, todo: TodoDomain) -> TodoDomain:
        existing_todo = Todo.query.get(todo.id)
        if existing_todo:
            existing_todo.title = todo.title
            existing_todo.description = todo.description
            existing_todo.priority = todo.priority
            existing_todo.due_date = todo.due_date
            db.session.commit()
            return ObjectMapperUtil.map(existing_todo, TodoDomain)
        return None

    def delete(self, todo_id: int) -> bool:
        todo = Todo.query.get(todo_id)
        if todo:
            db.session.delete(todo)
            db.session.commit()
            return True
        return False
