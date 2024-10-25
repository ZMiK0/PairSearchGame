import player
import board
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class Engine:
    '''
    This class is the engine of the game.

    Atributes:
    board (board): The board
    difficulty (int): The difficulty
    '''
    def __init__(self, _board: board.Board):
        '''
        Initializes the engine.

        Parameters:
        _board (board): Current game board.
        '''
        self.board = _board
        self.difficulty = 0
    
    def start(self):
        '''
        Starts the game.
        '''
        self.menu()

    def menu(self):
        '''
        Displays the menu and let the player choose the difficulty.
        '''
        ok = False
        while not ok:
            clear()
            option = input("Which gamemode would you like to play?\n1. 1v1\n2. 1vCPU\n3. CPUvCPU\n0. --EXIT--\n")
            if option == "2" or option == "3":
                ok2 = False
                while not ok2:
                    clear()
                    difficultyInput = (input("Set the bot difficulty\n1. Easy\n2. Medium\n3. Hard\nDifficulty: "))
                    match difficultyInput:
                        case "1":
                            self.difficulty = 1
                            ok2 = True
                        case "2":
                            self.difficulty = 2
                            ok2 = True
                        case "3":
                            self.difficulty = 3
                            ok2 = True
                        case (_):
                            print("Not an option")
                            input()
                                                    
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
                    name = input("Player name: ")
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
            if _player2.getScore() < self.board.getMaxPoints():
                self.playerTurn(_player1, _player2)
                if _player1.getScore() < self.board.getMaxPoints():
                    self.playerTurn(_player2, _player1)
                else:
                    print(f"THE WINNER IS: {_player1.getName()}")
                    game_over = True
            else:
                print(f"THE WINNER IS: {_player2.getName()}")
                game_over = True
        

    def playerTurn(self, _player: player.Player, _otherPlayer: player.Player):
        '''
        Manages the player's turn. If the player is not a bot, a position selection process is initiated, otherwise a random position is selected and added to both bot players memory.

        Parameters:
        _player (player): The player.
        _otherPlayer (player): The enemy player.
        '''
        positions = []
        if not _player.isThisABot():
            for i in range(2):
                ok = False
                while not ok:
                    clear()
                    print(f"Player: {_player.getName()}   Score: {_player.getScore()}")
                    self.board.printDisplayedBoard()
                    try:
                        pos1 = int(input("Row: "))-1
                        pos2 = int(input("Column: "))-1
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
            if self.difficulty == 3:
                _otherPlayer.addPlays((positions[0],positions[1]))
        else:
            ok = False
            while not ok:
                botPos1 = _player.botTurn(len(self.board.getBoard()),len(self.board.getBoard()[0]))
                botPos2 = _player.botTurn(len(self.board.getBoard()),len(self.board.getBoard()[0]))
                while not _player.checkPlays((botPos1,botPos2)):
                    botPos1 = _player.botTurn(len(self.board.getBoard()),len(self.board.getBoard()[0]))
                    botPos2 = _player.botTurn(len(self.board.getBoard()),len(self.board.getBoard()[0]))
                if (not self.board.isFlipped(botPos1) and not self.board.isFlipped(botPos2)) and (botPos1 != botPos2):
                    self.board.flipSymbol(botPos1)
                    self.board.flipSymbol(botPos2)
                    ok = True
            if self.difficulty == 2:
                _player.addPlays((botPos1,botPos2))
            elif self.difficulty == 3:
                _player.addPlays((botPos1,botPos2))
                _otherPlayer.addPlays((botPos1,botPos2))
            positions = [botPos1,botPos2]
                       
        clear()
        
        if self.board.checkSymbols(positions[0],positions[1]):
            _player.addScore()
            print(f"Player: {_player.getName()}   Score: {_player.getScore()}")
            self.board.printDisplayedBoard()
            input()
        else:
            print(f"Player: {_player.getName()}   Score: {_player.getScore()}")
            self.board.printDisplayedBoard()
            input()
            self.board.unflipSymbols(positions[0],positions[1])