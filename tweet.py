import tweepy
import time
#Verify the account 
auth = tweepy.OAuthHandler('xLngEgKUNT54D8whMGbv8X64Z','8Bp4bTD4Cx05oNILgMB5APjfbLyfjUVoEPmjJPFn1aV4usG0q3')
auth.set_access_token('1281592690098962433-HJ5ZhXm8qmEXBOC7oaWLbUxS4SpKBe', 'zegXS73paQMMHF7r3pp61TV14zcMwfVHrVwE0XwG65WRL')
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
    if follower.name == 'Ajeasmith':
        follower.follow()
        break
  