#!/usr/bin/env python3

import engine
import board
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear()
print("Welcome to PairSearchGame... Introduce the values of the board.\nWARNING: THIS WILL BE PERMANENT")
input("PRESS ENTER\n")
ok = False
while(not ok):
    clear()
    try:
        rows = int(input("Rows: "))
        columns = int(input("Columns: "))
    except:
        print("--WRONG, TRY AGAIN--")

    if (rows*columns)%2 == 0 and (rows*columns) <= 30 and rows > 0:
        ok = True
    else:
        print("Sorry, the product must be even and the board can't be bigger than 5x6 or 6x5...")
        input("PRESS ENTER")

game_board = board.Board(rows,columns)

game_engine = engine.Engine(game_board,)

game_engine.start()