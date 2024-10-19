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
        '''
        Starts the game.
        '''
        self.menu()

    def menu(self):
        '''
        Displays the menu.
        '''
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

    def play(self, _player1: player.Player, _player2: player.Player):
        '''
        Starts the secuence.

        Parameters:
        _player1 (player): Player1
        _player2 (player): PLayer2
        '''
        game_over = False
        self.board.buildBoard()
        self.board.buildDisplayedBoard()
        while not game_over:
            if _player1.getScore() < 2 and _player2.getScore() < 2:
                self.playerTurn(_player1)
                self.playerTurn(_player2)
            else:
                game_over = True
        

    def playerTurn(self, _player: player.Player):
        '''
        Manages the player's turn.

        Parameters:
        _player (player): The player.
        '''
        positions = []
        if not _player.isThisABot():
            for i in range(2):
                ok = False
                while not ok:
                    clear()
                    print(f"Player: {_player.getName()}")
                    self.board.printDisplayedBoard()
                    try:
                        pos1 = int(input("Row: "))
                        pos2 = int(input("Column: "))
                        if ((pos1 >= 0 and pos1 <= len(self.board.getBoard())) and (pos2 >= 0 and pos2 <= len(self.board.getBoard()[0]))) and not self.board.isFlipped((pos1,pos2)):
                            self.board.flipSymbol((pos1,pos2))
                            positions.append((pos1,pos2))
                            ok = True
                        else:
                            print("Out of limits or already flipped, try again...")
                            input()
                    except:
                        print("Not a number")
                        input()
        else:
            ok = False
            while not ok:
                botPos1 = _player.botTurn(len(self.board.getBoard()),len(self.board.getBoard()[0]))
                botPos2 = _player.botTurn(len(self.board.getBoard()),len(self.board.getBoard()[0]))
                if not self.board.isFlipped(botPos1) and not self.board.isFlipped(botPos2):
                    self.board.flipSymbol(botPos1)
                    self.board.flipSymbol(botPos2)
                    ok = True
            positions = [botPos1,botPos2]
            
        clear()
        print(f"Player: {_player.getName()}")
        self.board.printDisplayedBoard()
        input()
        if self.board.checkSymbols(positions[0],positions[1]):
            _player.addScore()
        else:
            self.board.unflipSymbols(positions[0],positions[1])

        
        
        
