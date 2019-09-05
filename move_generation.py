"""This module contains all the functions that 
   generates the computer's moves"""

from random import randint


def get_computer_move(computer_piece, board_state):
    arr = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    unavailable_moves = set()

    for move in board_state:
        unavailable_moves.add(int(move[1]))

    possible_moves = list(arr - unavailable_moves)
    
    chosen_move = possible_moves[randint(0, len(possible_moves) - 1)]
    return "{}{}".format(computer_piece, chosen_move)
    
