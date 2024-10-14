import random

class board:
    symbols = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    '''
    Tamaño dinamico
    3 modos de juego (1v1, 1vCpu, CpuvCpu)
    en cpu v cpu debe mostrarse los pasos, es decir, un metodo que printee el tablero actual
    '''
    board = []
    row = 0
    col = 0
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.addBoard()

    def addBoard(self):
        for i in range(self.row):
            a = []
            for j in range(self.col):
                a.append(random.sample(self.symbols, 1))
            self.board.append(a)
    
    def printBoard(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.board[i][j], end=" ")
            print()
        