from injector import Module, singleton, Binder
from core.todo.ports import ITodoAccessor
from infrastructure.todo.adapters import TodoAccessor

class TodoModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(ITodoAccessor, to=TodoAccessor, scope=singleton)
