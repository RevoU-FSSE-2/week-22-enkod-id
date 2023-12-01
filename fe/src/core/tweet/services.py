from injector import inject
from core.tweet.ports import ITweetAccessor
from core.user.ports import IUserAccessor

class TweetService():

    @inject
    def __init__(self, 
                 tweet_accessor: ITweetAccessor,
                 user_accessor: IUserAccessor,
                 ) -> None:
        self.tweet_accessor = tweet_accessor
        self.user_accessor = user_accessor

    def create_tweet(self, user_id:int, tweet:str, published_at:str):
        return self.tweet_accessor.create(user_id, tweet, published_at)
    
    def get_all(self):
        return self.tweet_accessor.get_all()