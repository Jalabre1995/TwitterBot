import tweepy
#Verify the account 
auth = tweepy.OAuthHandler('xLngEgKUNT54D8whMGbv8X64Z','8Bp4bTD4Cx05oNILgMB5APjfbLyfjUVoEPmjJPFn1aV4usG0q3')
auth.set_access_token('1281592690098962433-HJ5ZhXm8qmEXBOC7oaWLbUxS4SpKBe', 'zegXS73paQMMHF7r3pp61TV14zcMwfVHrVwE0XwG65WRL')

api = tweepy.API(auth)
user = api.me()

print(user.followers_count)