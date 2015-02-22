import threading
import time
import tweepy
import collections
import RobotListener
import json
import movement
import math
from tweepy import Stream
from tweepy.streaming import StreamListener


LEGAL_COMMANDS = ["forward", "backward", "left", "right"]

APP_KEY = "lgHnhvQExLozd24dliMg1jAlG"
APP_SECRET = "iesymLrCGhL8HcTLqyo0KSmYvZrxcfolqmi1Q06lnj5beHQEcU"
OAUTH_TOKEN = "3050210471-Ka1iB255E90jNpOVFLFIymGwqXVdQKEw8YgpNlk"
OAUTH_TOKEN_SECRET = "I67LL9hhAmcWobFD8qPaAY7YEKs2gdHlaL0IoOx3ggSmw"

queue = []

class RobotListener(StreamListener):

    def findLegalCommands(self, text):
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
    
    def on_data(self, data):
        print "Data:"
        jsonData = json.loads(data)
        command = self.findLegalCommands(jsonData['text'])
        print command
        queue.append(command)
        return True


class RobotThread (threading.Thread):
        def __init__(self, threadID, name, counter):
                threading.Thread.__init__(self)
                self.threadID = threadID
                self.name = name
                self.counter = counter
                self.queue = []

        def run(self):
                while True:
                        print len(queue)
                        if(len(queue) > 0):
                                command = queue.pop(0)
                                if command == LEGAL_COMMANDS[0]:
                                        movement.move(1)
                                        print "Moving forward"
                                elif command == LEGAL_COMMANDS[1]:
                                        movement.move(-1)
                                        print "Moving backward"
                                elif command == LEGAL_COMMANDS[2]:
                                        movement.turn(-math.pi/2.0)
                                        print "Moving left"
                                elif command == LEGAL_COMMANDS[3]:
                                        movement.turn(math.pi/2.0)
                                        print "Moving right"
                                                
                        time.sleep(5)


robotThread = RobotThread(1, "RobotThread", 1)
robotThread.start()

auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
robotStream = Stream(auth, RobotListener())
robotStream.filter(track=["@BlueberryPii"])


