from abc import ABC, abstractmethod
from typing import List
from core.todo.models import TodoDomain

class ITodoAccessor(ABC):

    @abstractmethod
    def create(self, title: str, description: str, priority: str, due_date: datetime) -> TodoDomain:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[TodoDomain]:
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self, todo_id: int) -> TodoDomain:
        raise NotImplementedError

    @abstractmethod
    def update(self, todo: TodoDomain) -> TodoDomain:
        raise NotImplementedError

    @abstractmethod
    def delete(self, todo_id: int) -> bool:
        raise NotImplementedError
