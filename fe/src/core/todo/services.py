from injector import inject
from core.todo.ports import ITodoAccessor

class TodoService:

    @inject
    def __init__(self, todo_accessor: ITodoAccessor):
        self.todo_accessor = todo_accessor

    def create_todo(self, title: str, description: str, priority: str, due_date: str):
        return self.todo_accessor.create(title, description, priority, due_date)

    def get_todo_list(self):
        return self.todo_accessor.get_all()

    def get_todo(self, todo_id: int):
        return self.todo_accessor.get_by_id(todo_id)

    def update_todo(self, todo_id: int, data: dict):
        todo = self.todo_accessor.get_by_id(todo_id)
        if todo:
            for key, value in data.items():
                setattr(todo, key, value)
            return self.todo_accessor.update(todo)
        return None

    def delete_todo(self, todo_id: int):
        return self.todo_accessor.delete(todo_id)
