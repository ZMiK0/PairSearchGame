import random

class Board:
    '''
    This class is the board of the game.

    Attributes:
    rows (int): Number of rows.
    columns (int): Number of columns.
    symbols (list): List of symbols.
    board (list): Board.
    displayed_board (list): The board the player see.
    max_points (int): The maximum points a player can get to win.
    '''

    def __init__(self, _row, _cols):
        '''
        Initializes the board.

        Parameters:
        _row (int): Number of rows.
        _cols (int): Number of columns.
        '''
        self.rows = _row
        self.columns = _cols
        self.symbols = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
        self.board = []
        self.displayed_board = []
        self.max_points = ((self.rows*self.columns)/2) + 2 #por ver

    def buildBoard(self):
        '''
        Builds the board and fill it's gaps.
        '''
        for i in range(self.rows):
            add = []
            for j in range(self.columns):
                add.append(None)
            self.board.append(add)

        for _ in range(int((self.rows*self.columns)/2)):
            self.setPairSymbol(self.getValidPos(),self.getSymbol())

    def buildDisplayedBoard(self):
        '''
        Builds the displayed board.
        '''
        for i in range(self.rows):
            addFalse = []
            for j in range(self.columns):
                addFalse.append("* ")
            self.displayed_board.append(addFalse)
        

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
        Returns valid positions in the board.
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
        '''
        Pops a symbol from the symbol list.
        '''
        return self.symbols.pop(self.symbols.index(random.sample(self.symbols,1)[0])) #Esto esta un poco guarro, revisar
    
    def printBoard(self):
        '''
        Prints the original board.
        '''
        self.buildBoard() #Eliminar esto cuando ya tenga el método play.
        for i in range(self.rows):
            for j in range(self.columns):
                print(' '.join(map(str, self.board[i][j])), end = "")
            print()

    def printDisplayedBoard(self):
        '''
        Prints the displayed board.
        '''
        self.buildDisplayedBoard() #Eliminar esto cuando ya tenga el método play.
        for i in range(self.rows):
            for j in range(self.columns):
                print(' '.join(map(str, self.displayed_board[i][j])), end = "")
            print()

    def flipSymbol(self, _pos):
        '''
        Flips a * in the displayed board.

        Parameters:
        _pos (int): Tuple of the position.
        '''
        self.displayed_board[_pos[0]][_pos[1]] = self.board[_pos[0]][_pos[1]]
    
    def unflipSymbols(self, _pos1, _pos2):
        '''
        Unflips a * in the displayed board.

        Parameters:
        _pos1 (int): Tuple of the first position.
        _pos1 (int): Tuple of the second position.
        '''
        self.displayed_board[_pos1[0]][_pos1[1]] = "* "
        self.displayed_board[_pos2[0]][_pos2[1]] = "* "
    
    def checkSymbols(self, _pos1, _pos2):
        '''
        Checks if the symbols are the same.

        Parameters:
        _pos1 (int): First position.
        _pos2 (int): Second position.

        Returns:
        true: If is correct and is not already flipped.
        false: If is the same position.
        false: If is not correct.
        '''
        if _pos1 != _pos2:
            if (self.board[_pos1[0]][_pos1[1]] == self.board[_pos2[0]][_pos2[1]]): # and not (self.isFlipped(_pos1) or self.isFlipped(_pos2)):
                return True
            else:
                return False
        else:
            return False
        
    def isFlipped(self, _pos):
        '''
        Checks if the position is already flipped.

        Returns:
        true: If the symbol is already displayed.
        false: If the symbol is not already displayed.
        '''
        if self.displayed_board[_pos[0]][_pos[1]] != "* ":
            return True
        else:
            return False
        
    def getBoard(self):
        '''
        Gets the board.
        '''
        return self.board



        
    #Hacer el método de cambiar una posicion de la tabla display por su simil de la tabla board
    #Hacer el método play



