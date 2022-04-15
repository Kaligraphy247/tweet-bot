import tweepy
import config


client = tweepy.Client(
    consumer_key=config.API_KEY,
    consumer_secret=config.API_KEY_SECRET,
    access_token=config.ACCESS_TOKEN,
    access_token_secret=config.ACCESS_TOKEN_SECRET)


print(client.get_user("James the Elder"))

# print(client.get_users_followers(id=))