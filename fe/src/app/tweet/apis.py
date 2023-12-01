# app.tweet.apis
from flask import Blueprint, request, jsonify
from core.tweet.services import TweetService
from core.common.utils import ObjectMapperUtil
from datetime import datetime

tweet_blueprint = Blueprint("tweet_blueprint", __name__)
tweet_service = TweetService()  


@tweet_blueprint.route("", methods=["POST"])
def post_tweet():
    tweet_content = request.json.get("tweet")

    if tweet_content:
        user_id = 1
        published_at = datetime.now()

        new_tweet = tweet_service.create_tweet(user_id=user_id, tweet=tweet_content, published_at=published_at)
        return jsonify(new_tweet), 201
    else:
        return jsonify({"error": "Tweet content not found"}), 400
    
@tweet_blueprint.route("", methods=["GET"])
def get_all_tweets():
    all_tweets = tweet_service.get_all()

    if all_tweets:
        
        return jsonify(ObjectMapperUtil.map(all_tweets)), 200
    else:
        return jsonify({"error": "No tweets found"}), 404 