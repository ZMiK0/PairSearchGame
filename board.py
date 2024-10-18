import random

class Board:
    '''
    This class is the engine of the game.

    Attributes:
    rows (int): Number of rows.
    columns (int): Number of columns.
    symbols (list): List of symbols.
    board (list): Board.
    '''

    def __init__(self, _row, _cols):
        '''
        Initializes the engine.

        Parameters:
        _row (int): Number of rows.
        _cols (int): Number of columns.
        '''
        self.rows = _row
        self.columns = _cols
        self.symbols = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
        self.board = []

    def buildBoard(self):
        '''
        Builds the board.
        '''
        for i in range(self.rows):
            add = []
            for j in range(self.columns):
                add.append(None)
            self.board.append(add)

        for _ in range(int((self.rows*self.columns)/2)):
            self.setPairSymbol(self.getValidPos(),self.getSymbol())
        

    def setPairSymbol(self, _pos, _symbol):
        '''
        Sets a pair of symbols in the board.

        Parameter:
        _pos (list): Positions list.
        _symbol (str): Symbol.
        '''
        self.board[_pos[0][0]][_pos[0][1]] = _symbol
        self.board[_pos[1][0]][_pos[1][1]] = _symbol


    def getValidPos(self):
        '''
        Returns void positions in the board.
        '''
        pos1 = random.randint(0,self.rows-1)
        pos2 = random.randint(0,self.columns-1)
        while(self.board[pos1][pos2] is not None):
            pos1 = random.randint(0,self.rows-1)
            pos2 = random.randint(0,self.columns-1)
        
        pos3 = random.randint(0,self.rows-1)
        pos4 = random.randint(0,self.columns-1)
        while(self.board[pos3][pos4] is not None or (pos3,pos4) == (pos1,pos2)):
            pos3 = random.randint(0,self.rows-1)
            pos4 = random.randint(0,self.columns-1)

        return [(pos1,pos2),(pos3,pos4)]
    
    def getSymbol(self):
        return self.symbols.pop(self.symbols.index(random.sample(self.symbols,1)[0])) #Esto esta un poco guarro, revisar
    
    def printBoard(self):
        self.buildBoard()
        for i in range(self.rows):
            for j in range(self.columns):
                print(' '.join(map(str, self.board[i][j])), end = "")
            print()
        




        
    #Hacer método getValidPos() para hacer pos1 = getValidPos()
    #La board quedaba [[,,,,],[,,,,],[,,,,],[,,,,]]


    

    
