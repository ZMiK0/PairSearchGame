import random

class board:
    symbols = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
    '''
    Tamaño dinamico
    3 modos de juego (1v1, 1vCpu, CpuvCpu)
    en cpu v cpu debe mostrarse los pasos, es decir, un metodo que printee el tablero actual
    '''
    board = []
    display_board = []
    row = 0
    col = 0
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.addBoard()

    def addBoard(self):
        for i in range(self.row):
            a = []
            da = []
            for j in range(self.col):
                a.append(random.sample(self.symbols, 1))
                da.append("x")
            self.board.append(a)
            self.display_board.append(da)
    
    def printBoard(self):
        for i in range(self.row):
            for j in range(self.col):
                print(' '.join(map(str, self.board[i][j])), end=" ",)
            print()

    def printDisplayBoard(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.display_board[i][j], end=" ")
            print()
        