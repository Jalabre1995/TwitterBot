import tweepy
import time
#Verify the account by putting in your api key, and secret api key
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#Verify the access token and secret access token. 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.me()

def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(3000)
#Generous Bot 
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    if follower.followers_count > 100:
       follower.follow()
       break



# Narcisistic
search_string = 'python'
numbersOfTweets = 2
for tweet in limit_handle(tweepy.Cursor(api.search, search_string).items(numbersOfTweets)):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
            break
