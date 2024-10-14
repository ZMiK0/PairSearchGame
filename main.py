import board
import os

def clear():
    os.system("clear")

end = False

row = int(input("Rows: "))
col = int(input("Columns: "))
gm = board.board(row, col)
clear()
gm.printBoard()
input("")

while not end:
    
    clear()    

    gm.printDisplayBoard()

    gm.selectPos()