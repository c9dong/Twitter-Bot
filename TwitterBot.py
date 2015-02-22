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

def findLegalCommands(text):
        indexes = []
        for _command in LEGAL_COMMANDS:
            indexes.append(text.upper().find(_command.upper()))
            #if not (text.upper().find(_command.upper()) == -1):
                #return _command
        minn = indexes[0]
        minIndex = 0
        for i in range(len(indexes)):
            if not indexes[i] == -1:
                if indexes[i] < minn or minn == -1:
                    minn = indexes[i]
                    minIndex = i
        if minn == -1:
        	return ""
        else:
            return LEGAL_COMMANDS[minIndex]

auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

mentions = api.mentions_timeline(count=10)

arrayOfCommands = [] 
for mention in mentions:
	validCommand = findLegalCommands(mention.text)
	if not validCommand == "":
		arrayOfCommands.append(validCommand)


print arrayOfCommands


##class RobotListener(StreamListener):
##    
##    def findLegalCommands(self, text):
##        indexes = []
##        for _command in LEGAL_COMMANDS:
##            indexes.append(text.upper().find(_command.upper()))
##            #if not (text.upper().find(_command.upper()) == -1):
##                #return _command
##        minn = indexes[0]
##        minIndex = 0
##        for i in range(len(indexes)):
##            if not indexes[i] == -1:
##                if indexes[i] < minn:
##                    minn = indexes[i]
##                    minIndex = i
##        if minn == -1:
##            return ""
##        else:
##            return LEGAL_COMMANDS[minIndex]
##
##    def on_data(self, data):
##        jsonData = json.loads(data)
##        print self.findLegalCommands(jsonData['text'])
##        return True

##robotStream = Stream(auth, RobotListener())
##robotStream.filter(track=["@ChristieBond007"])
