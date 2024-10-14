import board
import os

def clear():
    os.system("clear")

end = False


player1Name = input("Player1: ")
player2Name = input("Player2: ")

row = int(input("Rows: "))
col = int(input("Columns: "))
gm = board.board(row, col, player1Name, player2Name)
clear()
gm.printBoard()
input("")
while not end:
    clear()    
    gm.turns()