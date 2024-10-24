import random

class Player:
    '''
    This is the player class.

    Attributes:
    score (int): Score of the player.
    name (str): Name of the player.
    isBot (boolean): Bot status.
    '''

    def __init__(self, _name, _isBot):
        '''
        Initializes the player.

        Parameters:
        _name (str): Player name.
        _isBot (boolean): Determines if the player is a bot.
        '''
        self.score = 0
        self.name = _name
        self.isBot = _isBot
        self.plays = []

    def addScore(self):
        '''
        It adds one point to the score.
        '''
        self.score += 1
    
    def getName(self):
        '''
        Gets the player's name.

        Returns:
        str: Player name
        '''
        return self.name
    
    def getScore(self):
        '''
        Gets the player's score.

        Returns:
        int: Player score
        '''
        return self.score
    
    def botTurn(self, _maxRow, _maxCol):
        '''
        Imitate the player action. NOT FINISHED

        Parameters:
        _maxRow (int): Max number of board rows.
        _maxCol (int): Max number of board columns.

        Returns:
        int: Tuple of positions.
        '''
        pos1 = random.randint(0,_maxRow-1)
        pos2 = random.randint(0,_maxCol-1)

        return (pos1,pos2)

    def isThisABot(self):
        '''
        Returns the humanity of the player.
        '''
        return self.isBot
    
    def addPlays(self, _tuple): #Tiene que entrarle la play del rival también xd
        '''
        Adds a position tuple in plays list for a simple bot memory.
        '''
        self.plays.append(_tuple)
    
    def checkPlays(self, _plays):
        '''
        Cheks is said play was already made.

        Returns:
        True: If the plays list is empty.
        False: If the play was already made.
        True: If the play is new.
        '''
        if len(self.plays) != 0:
            for i in self.plays:
                if _plays != i:
                    return True
                else:
                    return False
        else:
            return True