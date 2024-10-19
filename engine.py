import player
import board
import os

def clear():
    os.system('clear')

class Engine:
    '''
    This class is the engine of the game.

    Atributes:
    board (board): 
    '''
    def __init__(self, _board: board.Board):
        '''
        Initializes the engine.

        Parameters:
        _board (board): Current game board.
        '''
        self.board = _board
    
    def start(self):
        self.menu()

    def menu(self):
        ok = False
        while not ok:
            clear()
            option = input("Which gamemode would you like to play?\n1. 1v1\n2. 1vCPU\n3. CPUvCPU\n0. --EXIT--\n")
            match option:
                case "0":
                    ok = True
                case "1":
                    clear()
                    name = input("Player1 name: ")
                    p1 = player.Player(name, False)
                    name = input("Player2 name: ")
                    p2 = player.Player(name, False)
                    ok = True
                case "2":
                    clear()
                    name = input("Player1 name: ")
                    p1 = player.Player(name, False)
                    p2 = player.Player("CPU", True)
                    ok = True
                case "3":
                    clear()
                    p1 = player.Player("CPU1", True)
                    p2 = player.Player("CPU2", True)
                    ok = True
                case (_):
                    print("--Wrong Option--")
                    input()
        if option != "0":
            self.play(p1,p2)
        else:
            clear()
            print("--Ending the game--")
            input()

    def play(self, player1: player.Player, player2: player.Player):
        self.board.buildBoard()
        self.board.buildDisplayedBoard()
        
