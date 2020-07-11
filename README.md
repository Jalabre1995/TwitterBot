# TwitterBot

The purpose of this project is to create fun twitter bots that you can use on your twitter account. As a user that has a twitter account myself, I am always busy and never have time to check my twitter account. With the help of a Twitter bot it does the work for me while I attend my daily schedule. 

# Imports
Make sure to import:
pip install tweepy
pip install time(already built into python)

# API
Twitter API is used for this project. To make sure you are able to use Twitter's API, make sure you create account for the Twitter API to get an API key.

# Getting started 
Go on to tweepy and click on getting started. 
Copy this in your python file:
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
    
# Still in Progress
There is so much to explore with the Twitter API, but for now, I created a generous bot that follows users that have more than 100 followers and a narcisistic bot that likes a user's comment based on the keyword you put in the search_string.
  


