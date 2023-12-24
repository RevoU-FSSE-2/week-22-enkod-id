from abc import ABC, abstractmethod
from typing import List
from core.todo.models import TodoDomain  # replace with your actual TodoDomain import

class ITodoAccessor(ABC):

    @abstractmethod
    def create(self, title: str, description: str, priority: str, dueDate: str) -> TodoDomain:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[TodoDomain]:
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self, id: int) -> TodoDomain:
        raise NotImplementedError

    @abstractmethod
    def update(self, id: int, title: str, description: str, priority: str, dueDate: str) -> TodoDomain:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int) -> None:
        raise NotImplementedError