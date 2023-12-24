from injector import Module, singleton, Binder
from core.todo.ports import ITodoAccessor  # replace with your actual ITodoAccessor import
from infrastructure.todo.adapters import TodoAccessor  # replace with your actual TodoAccessor import

class TodoModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(ITodoAccessor, to=TodoAccessor, scope=singleton)