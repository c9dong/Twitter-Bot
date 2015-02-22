import tweepy
import random

CONSUMER_KEY ="itYOsydZ0l3riSjA2R3bZJ48H"
CONSUMER_SECRET = "lDEa4dzT8UuWUeX6csw14rvRWKsJoyQhrI9bAEVmo15u1Qm9BJ"   
ACCESS_KEY = "2830802468-wH6T4NOYEJ64vIyjO43nTKLP8pUvUmwEOMS99Yd"    
ACCESS_SECRET = "y8UiOKQvGRmsAsdqoY8RlSTCd3Pvj0nmIi8OJFwAMkWwv"

LEGAL_COMMANDS = ["forward", "backward", "left", "right"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

# automated tweets for demo purposes
for n in range(1):
    randomNum = random.randint(-1,3)
    appendNum = random.randint(0,5000)

    randomCommand = LEGAL_COMMANDS[randomNum]
    tweet = "@ChristieBond007 "+ randomCommand + str(appendNum)


    api.update_status(status = tweet)
