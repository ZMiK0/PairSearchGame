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
    
    def botTurn(self):
        '''
        Imitate the player action. NOT FINISHED
        '''
        pass
    