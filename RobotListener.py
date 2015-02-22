from tweepy import Stream
from tweepy.streaming import StreamListener

LEGAL_COMMANDS = ["forward", "backward", "left", "right"]

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
        jsonData = json.loads(data)
        print self.findLegalCommands(jsonData['text'])
        return True
