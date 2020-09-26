# Milestone Project 1

import random
#from IPython.display import clear_output
'''To clear the screen between moves:
from IPython.display import clear_output
clear_output()
Note that clear_output() will only work in jupyter.
To clear the screen in other IDEs, consider:
print('\n'*100)
This scrolls the previous board up out of view. Now on to the program!'''

def display_board(board):
    print(board[7], "|", board[8], "|", board[9])
    print(board[4], "|", board[5], "|", board[6])
    print(board[1], "|", board[2], "|", board[3])


def player_input():
    choice = ''
    valid = ['x', 'X', 'o', 'O']
    while choice not in valid:
        choice = input("Player 1, choose your destiny! Will you be X or O? ")

    if choice == 'x' or choice == 'X':
        player_1 = 'X'
        player_2 = 'O'
    else:
        player_1 = 'O'
        player_2 = 'X'

    return (player_1, player_2)


def choose_first():
    plays_first = random.randint(1, 2)
    if plays_first == 1:
        return "Player 1, you play first!"
    else:
        return "Player 2, you play first!"


def place_marker(board, marker, position):
    board[int(position)] = marker


def space_check(board, position):
    return (board[int(position)] != 'X' and board[int(position)] != 'O')


def player_choice(board):
    free = False
    position = '0'
    while not free:
        position = input("Choose a free spot on the board (from 1 to 9): ")
        if position.isdigit() and int(position) >= 1 and int(position) <= 9:
            if space_check(board, position):
                return position
        else:
            print("Please choose a valid, free position.")


def win_check(board, mark):
    # Checking lines
    for i in [1, 4, 7]:
        if board[i] == board[i+1] == board[i+2] == mark:
            return True
    # Checking columns
    for i in [1, 2, 3]:
        if board[i] == board[i+3] == board[i+6] == mark:
            return True
    # Checking diagonals
    if board[7] == board[5] == board[3] == mark:
        return True
    if board[9] == board[5] == board[1] == mark:
        return True
    return False


def full_board_check(board):
    for i in range(1, len(board)):
        if board[i] != 'X' and board[i] != 'O':
            return False
    print("Full board!")
    return True


def replay():
    valid = ['y', 'Y', 'n', 'N']
    choice = ''
    while choice not in valid:
        choice = input("Would you like to play again? [Y, N] ")
    if choice == 'y' or choice == 'Y':
        return True
    return False


# Here we go!
print('Welcome to Tic Tac Toe!')

lets_play = True

while lets_play:
    # Setting up the game
    board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    display_board(board)

    # Getting the players ready to roll
    P1, P2 = player_input()
    print(choose_first())

    game_on = True
    current_player = P1

    while game_on:
        choice = player_choice(board)
        place_marker(board, current_player, choice)
        display_board(board)
        if win_check(board, current_player) or full_board_check(board):
            game_on = False
            if win_check(board, current_player):
                print(current_player + " wins!")
        else:
            if current_player == P1:
                current_player = P2
            else:
                current_player = P1
        if game_on:
            print("Next player!")


    lets_play = replay()
