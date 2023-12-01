from abc import ABC, abstractmethod
from typing import List
from core.tweet.models import TweetDomain

class ITweetAccessor(ABC):

    @abstractmethod
    def create(self, user_id: int, tweet: str, publised_at: str) -> TweetDomain:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[TweetDomain]:
        raise NotImplementedError  