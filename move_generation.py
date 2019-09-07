"""This module contains all the functions that 
   generates the computer's moves"""

from random import randint


def get_computer_move(computer_piece, board_state):
    """Function that generates computer moves based off of 
       Newell and Simon's 1972 Tic-Tac-Toe program explain here:
       https://en.wikipedia.org/wiki/Tic-tac-toe#Strategy"""

    check_one = play_win(computer_piece, board_state)

    if check_one != None:
        return check_one

    check_two = block_win(computer_piece, board_state)

    if check_two != None:
        return check_two

    check_three = play_fork(computer_piece, board_state)

    if check_three != None:
        return check_three

    check_four = block_fork(computer_piece, board_state)

    if check_four != None:
        return check_four

    check_five = play_center(computer_piece, board_state)

    if check_five != None:
        return check_five

    check_six = play_opposite_corner(computer_piece, board_state)

    if check_six != None:
        return check_six

    check_seven = play_empty_corner(computer_piece, board_state)

    if check_seven != None:
        return check_seven

    check_eight = play_empty_side(computer_piece, board_state)

    if check_eight != None:
        return check_eight


def play_win(computer_piece, board_state):
    """If there is a win on the board for the computer, play it"""

    # List containing all possible winning combinations
    possible_wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                     [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    
    # Create a list of moves played by both players so far
    computer_move_history = []
    user_move_history = []

    # Append all the computer moves to computer_move_history
    for move in board_state:
        if move[0] == computer_piece:
            computer_move_history.append(int(move[1]))

        else:
            user_move_history.append(int(move[1]))
    
    # Append all the moves to the list where they belong
    for win in possible_wins:
        counter = 0

        for move in computer_move_history:
            if move in win:
                counter += 1
        
        if counter == 2:
            for square in win:
                if square not in computer_move_history and square not in user_move_history:
                    return "{}{}".format(computer_piece, square)
    
    # Return None if there is no immediate win in the current position
    return None
        

def block_win(computer_piece, board_state):
    """If there is a win on the board for the user, block it"""

    # List containing all possible winning combinations
    possible_wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                     [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    
    # Create a list of moves played by both players so far
    computer_move_history = []
    user_move_history = []

    # Append all the moves to the list where they belong
    for move in board_state:
        if move[0] != computer_piece:
            user_move_history.append(int(move[1]))

        else:
            computer_move_history.append(int(move[1]))
    
    # Check which win has two squares filled and play the missing one
    for win in possible_wins:
        counter = 0

        for move in user_move_history:
            if move in win:
                counter += 1
        
        if counter == 2:
            for square in win:
                if square not in user_move_history and square not in computer_move_history:
                    return "{}{}".format(computer_piece, square)
    
    # Return None if there is no immediate win in the current position
    return None


def play_fork(computer_piece, board_state):
    """If there is a fork on the board for the computer, play it"""

    # List containing all possible forks
    possible_wins = [[1, 3, 7], [1, 3, 9], [1, 7, 9], [3, 7, 9],
                     [2, 4, 5], [2, 4, 6], [4, 5, 8], [5, 6, 8],
                     [5, 8, 9], [5, 7, 8], [1, 2, 5], [2, 3, 5],
                     [4, 7, 9], [4, 8, 9], [6, 7, 8], [6, 7, 9],
                     [1, 2, 6], [1, 3, 6], [3, 4, 5], [3, 4, 6]]
    
    # Create a list of moves played by both players so far
    computer_move_history = []
    user_move_history = []

    # Append all the computer moves to computer_move_history
    for move in board_state:
        if move[0] == computer_piece:
            computer_move_history.append(int(move[1]))

        else:
            user_move_history.append(int(move[1]))
    
    # Append all the moves to the list where they belong
    for win in possible_wins:
        counter = 0

        for move in computer_move_history:
            if move in win:
                counter += 1
        
        if counter == 2:
            for square in win:
                if square not in computer_move_history and square not in user_move_history:
                    print(win)
                    return "{}{}".format(computer_piece, square)
    
    # Return None if there is no immediate win in the current position
    return None


def block_fork(computer_piece, board_state):
    """If there is a win on the board for the user, block it"""

    # List containing all possible winning combinations
    possible_wins = [[1, 3, 7], [1, 3, 9], [1, 7, 9], [3, 7, 9],
                     [2, 4, 5], [2, 4, 6], [4, 5, 8], [5, 6, 8],
                     [5, 8, 9], [5, 7, 8], [1, 2, 5], [2, 3, 5],
                     [4, 7, 9], [4, 8, 9], [6, 7, 8], [6, 7, 9],
                     [1, 2, 6], [1, 3, 6], [3, 4, 5], [3, 4, 6]]
    
    # Create a list of moves played by both players so far
    computer_move_history = []
    user_move_history = []

    # Append all the moves to the list where they belong
    for move in board_state:
        if move[0] != computer_piece:
            user_move_history.append(int(move[1]))

        else:
            computer_move_history.append(int(move[1]))
    
    # Check which win has two squares filled and play the missing one
    for win in possible_wins:
        counter = 0

        for move in user_move_history:
            if move in win:
                counter += 1
        
        if counter == 2:
            for square in win:
                if square not in user_move_history and square not in computer_move_history:
                    return "{}{}".format(computer_piece, square)
    
    # Return None if there is no immediate win in the current position
    return None


def play_center(computer_piece, board_state):
    """Play in the center if it is available"""

    for move in board_state:
        if int(move[1]) == 5:
            return None
    
    return "{}5".format(computer_piece)


def play_opposite_corner(computer_piece, board_state):
    """Play on the corner opposite of the user's last move"""

    # All the possible corner pairs in Tic-Tac-Toe
    corner_pairs = [[1, 9], [3, 7]]

    squares_played = []
    last_square_played = int(board_state[-1][1])

    # Get all the squares from the board_state so we can check availability
    for move in board_state:
        squares_played.append(int(move[1]))

    # Check if the last move played is on a corner
    for pair in corner_pairs:
        if last_square_played in pair:
            pair.remove(last_square_played)

            # Return the opposite corner if it is available
            if pair[0] not in squares_played:
                return "{}{}".format(computer_piece, pair[0])
            
            else:
                return None
    
    return None


def play_empty_corner(computer_piece, board_state):
    """If there is an empty corner, put a piece there"""

    available_corners = [1, 3, 7, 9]

    # Remove corner from available_corners if it is already taken
    for move in board_state:
        if int(move[1]) in available_corners:
            available_corners.remove(int(move[1]))
    
    # Check that there is a corner available
    if len(available_corners) != 0:
        corner = available_corners[randint(0, len(available_corners) - 1)]
        return "{}{}".format(computer_piece, corner)
    
    else:
        return None


def play_empty_side(computer_piece, board_state):
    """If there is an empty side, put a piece there"""

    available_sides = [2, 4, 6, 8]

    # Remove side from available_sides if it is already taken
    for move in board_state:
        if int(move[1]) in available_sides:
            available_sides.remove(int(move[1]))
    
    # Check that there is a side available
    if len(available_sides) != 0:
        side = available_sides[randint(0, len(available_sides) - 1)]
        return "{}{}".format(computer_piece, side)
    
    else:
        return None