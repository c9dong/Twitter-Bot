import time
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import json

LEGAL_COMMANDS = ["forward", "backward", "left", "right"]

APP_KEY = "lgHnhvQExLozd24dliMg1jAlG"
APP_SECRET = "iesymLrCGhL8HcTLqyo0KSmYvZrxcfolqmi1Q06lnj5beHQEcU"
OAUTH_TOKEN = "3050210471-Ka1iB255E90jNpOVFLFIymGwqXVdQKEw8YgpNlk"
OAUTH_TOKEN_SECRET = "I67LL9hhAmcWobFD8qPaAY7YEKs2gdHlaL0IoOx3ggSmw"

class RobotListener(StreamListener):
    
    def findLegalCommands(self, text):
        for _command in LEGAL_COMMANDS:
            if not (text.upper().find(_command.upper()) == -1):
                return _command
        return ""

    def on_data(self, data):
        jsonData = json.loads(data)
        print self.findLegalCommands(jsonData['text'])
        return True

auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

robotStream = Stream(auth, RobotListener())
robotStream.filter(track=["@ChristieBond007"])
