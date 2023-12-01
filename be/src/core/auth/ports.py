from abc import ABC, abstractmethod

class IHashingProvider(ABC):

    @abstractmethod
    def generate(self, value:str) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def check_hash(self, hashed_value: str, value: str) -> bool:
        raise NotImplementedError