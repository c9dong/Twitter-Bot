import time
import tweepy
import collections
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import movement
import math

LEGAL_COMMANDS = ["forward", "backward", "left", "right"]

APP_KEY = "lgHnhvQExLozd24dliMg1jAlG"
APP_SECRET = "iesymLrCGhL8HcTLqyo0KSmYvZrxcfolqmi1Q06lnj5beHQEcU"
OAUTH_TOKEN = "3050210471-Ka1iB255E90jNpOVFLFIymGwqXVdQKEw8YgpNlk"
OAUTH_TOKEN_SECRET = "I67LL9hhAmcWobFD8qPaAY7YEKs2gdHlaL0IoOx3ggSmw"

def findLegalCommands(text):
        indexes = []
        for _command in LEGAL_COMMANDS:
            indexes.append(text.upper().find(_command.upper()))
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

while True:
    mentions = api.mentions_timeline(count=10)

    arrayOfCommands = [] 
    for mention in mentions:
        validCommand = findLegalCommands(mention.text)
        if not validCommand == "":
            arrayOfCommands.append(validCommand)
    #print arrayOfCommands
    command = collections.Counter(arrayOfCommands).most_common(1)[0][0]
    if command == LEGAL_COMMANDS[0]:
        movement.move(1)
    elif command == LEGAL_COMMANDS[1]:
        movement.move(-1)
    elif command == LEGAL_COMMANDS[2]:
        movement.turn(-math.PI/2.0)
        movement.move(1)
    elif command == LEGAL_COMMANDS[3]:
        movement.turn(math.PI/2.0)
        movement.move(1)
                
    time.sleep(10)
