class Player():
    name = ""
    score = 0
    def __init__(self, name):
        self.name = name
        self.score = 0

    def getName(self):
        return self.name
    
    def setScorePlusOne(self):
        self.score += 1

    def getScore(self):
        return self.score