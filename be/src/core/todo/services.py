from injector import inject
from core.todo.ports import ITodoAccessor  # replace with your actual ITodoAccessor import

class TodoService():

    @inject
    def __init__(self, todo_accessor: ITodoAccessor) -> None:
        self.todo_accessor = todo_accessor

    def create_todo(self, title:str, description:str, priority:str, dueDate:str):
        return self.todo_accessor.create(title, description, priority, dueDate)

    def get_todo_list(self):
        return self.todo_accessor.get_all()

    def get_todo(self, id: int):
        return self.todo_accessor.get_by_id(id)

    def update_todo(self, id: int, title:str, description:str, priority:str, dueDate:str):
        return self.todo_accessor.update(id, title, description, priority, dueDate)

    def delete_todo(self, id: int):
        return self.todo_accessor.delete(id)