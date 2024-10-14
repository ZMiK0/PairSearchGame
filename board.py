import random
import os
import player

def clear():
    os.system("clear")

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

    turn = 0

    player1 = None
    player2 = None

    def __init__(self, row, col, p1, p2):
        self.row = row
        self.col = col
        self.player1 = player.Player(p1)
        self.player2 = player.Player(p2)
        self.__addBoard__()

    def __addBoard__(self):
        for i in range(self.row):
            a = []
            da = []
            for j in range(self.col):
                a.append(random.sample(self.symbols, 1))
                da.append(" ")
            self.board.append(a)
            self.display_board.append(da)
    
    def printBoard(self):
        for i in range(self.row):
            for j in range(self.col):
                print(' '.join(map(str, self.board[i][j])), end=" ",)
            print()

    def printDisplayBoard(self):
        if self.turn == 0:
            print(self.player1.getName())
        else: 
            print(self.player2.getName())
        for i in range(self.row):
            for j in range(self.col):
                print(' '.join(map(str, self.display_board[i][j])), end=" ",)
            print()

    def selectPos(self):
        pi = int(input("Pos1: "))-1
        pj = int(input("Pos2: "))-1

        try: 
            self.__updatePos__(pi,pj)
            return (pi,pj)
        except:
            print("--ERROR--")
    
    def __updatePos__(self, pi, pj):
        self.display_board[pi][pj] = self.board[pi][pj]

    def turns(self):
        values = []
        for i in range(2):
            clear()
            self.printDisplayBoard()
            values.append(self.selectPos())
        try: 
            if self.turn == 0:
                if self.__checkPos__(values):
                    self.player1.setScorePlusOne()
                else:
                    pass
                self.turn = 1
            else:
                if self.__checkPos__(values):
                    self.player2.setScorePlusOne()
                else:
                    pass
                self.turn = 0
        except:
            print("--ERROR-- TRY")

        

    def __checkPos__(self, values):
        if self.board[values[0][0]][values[0][1]] == self.board[values[1][0]][values[1][1]]:
            return True
        else: 
            return False
        
