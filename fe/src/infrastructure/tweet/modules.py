from injector import Module, singleton, Binder
from core.tweet.ports import ITweetAccessor
from infrastructure.tweet.adapters import TweetAccessor

class JobModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(ITweetAccessor, to=TweetAccessor, scope=singleton)