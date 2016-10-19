#A command line version of Anti-Minesweeper
#Author: Janusz
#Date: 19 Oct 2016

from random import randint
from string import ascii_lowercase
from itertools import product

board = []
for i in range(9):
    board.append(['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'])

def print_board(board):
    board_length = len(board)
    print("    ", end="")
    for i in range(board_length):
        print(i, end = ' ')       #printing column indices at the top
    print("\n")

    #for row, i in product(board, range(9)):       #This `product` is making the iteration very large
    for i, row in enumerate(board):
        print(i, end='   ')
        print(' '.join(row))
        #if(i == 8):
            #print("\n")
            #break           #This is just a hack to stop the board getting printed very long

def random_row():       #This function returns random position of the row
    return randint(0, 8)

def random_col():       #This function returns random position of the column
    return randint(0, 8)

def guess_row():
    return int(input("Row Guess: "))

def guess_col():
    return int(input("Column Guess: "))

def play_game():
    print("Welcome to Anti-Minesweeper. This game has a simple rule. You need to guess 3 out of 9 battleships to defeat "
          "enemy. For this you have 9 chances to eliminate those battleships.\n")
    print_board(board)
    print("Start making some guesses. Let's roll. :) ")
    ship_posi = set()

    for i in range(9):
        row_posi = random_row()
        col_posi = random_col()
        ship_posi.add((row_posi, col_posi))

    #print(ship_posi)
    count = 0
    i = 0
    while i<9:
        if (count == 3):
            print("You are awesome! You won.")
            break
        print("Turn: " + str(i+1))
        row_guess = guess_row()
        col_guess = guess_col()
        if row_guess > 8 or col_guess > 8:
            print("Hey, you went into non-war zone. Get back to the battlefield!")
        elif board[row_guess][col_guess] == 'X' or board[row_guess][col_guess] == 'B':
            print("You have already bombed this place. Try some other place.")
        elif (row_guess, col_guess) in ship_posi:
            count += 1
            i += 1
            board[row_guess][col_guess] = "B"
            print("Good. You need to find {} more battleships to defeat the enemy".format(3-count))
        else:
            board[row_guess][col_guess] = "X"
            i += 1
            print("Oops, you missed. It's okay, you just need to find {} battleships to defeat the enemy".format(3-count))

        print_board(board)

play_game()