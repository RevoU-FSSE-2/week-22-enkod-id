from typing import List
from core.tweet.models import TweetDomain
from core.tweet.ports import ITweetAccessor
from infrastructure.db import db
from infrastructure.tweet.models import Tweet
from core.common.utils import ObjectMapperUtil

class TweetAccessor(ITweetAccessor):
    
    def create(self, user_id: int, tweet: str) -> TweetDomain:
        new_tweet = Tweet(user_id=user_id, tweet=tweet)
        db.session.add(new_tweet)
        db.session.commit()

        return ObjectMapperUtil.map(new_tweet, TweetDomain)
    
    def get_all(self) -> List[TweetDomain]:
        tweets = Tweet.query.all()
        return [ObjectMapperUtil.map(tweet, TweetDomain) for tweet in tweets]