from dataclasses import dataclass 

@dataclass
class TweetDomain:
    id: int
    user_id: int
    tweet: str
    published_at: str