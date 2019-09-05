"""This module contains all the functions for the game loop except for 
   the code that generates the computer's moves"""

from move_generation import get_computer_move


def game_loop(user_piece, computer_piece):
    """Main game loop which handles everything from displaying the board, 
       taking a user move, generating a computer response, and checking 
       the board state"""
    
    # Board state contains all the moves played in the game thus far
    board_state = []

    while True:
        show_board(board_state)

        # TODO: Refactor this code to be less messy (I copy pasted stuff)
        if user_piece == "X":
            user_move = get_user_move(user_piece, board_state)
            board_state.append(user_move)
            result = check_board(user_piece, board_state)
            show_board(board_state)

            if result != "incomplete":
                print("You {} the game!".format(result))
                return restart()

            computer_move = get_computer_move(computer_piece, board_state)
            board_state.append(computer_move)
            print("The computer played {}!".format(computer_move))
            result = check_board(user_piece, board_state)

            if result != "incomplete":
                print("You {} the game!".format(result))
                return restart()


        else:
            computer_move = get_computer_move(computer_piece, board_state)
            board_state.append(computer_move)
            print("The computer played {}!".format(computer_move))
            show_board(board_state)
            result = check_board(user_piece, board_state)

            if result != "incomplete":
                print("You {} the game!".format(result))
                return restart()

            user_move = get_user_move(user_piece, board_state)
            board_state.append(user_move)
            result = check_board(user_piece, board_state)
            show_board(board_state)

            if result != "incomplete":
                print("You {} the game!".format(result))
                return restart()

        if result != "incomplete":
            show_board(board_state)
            print("You {} the game!".format(result))
            return restart()


def show_board(board_state):
    """Given a list of moves in tic-tac-toe notation, show the board"""

    # Top margin
    print()

    # Here, the board is represented as a 2D matrix
    board = [["[ ]", "[ ]", "[ ]"], 
             ["[ ]", "[ ]", "[ ]"], 
             ["[ ]", "[ ]", "[ ]"]]

    # Iterate through all moves in the moves list and add to board
    for move in board_state:
        piece = move[0]
        square = int(move[1])

        if square in [1, 2, 3]:
            board[0][square - 1] = "[{}]".format(piece)

        elif square in [4, 5, 6]:
            board[1][square - 4] = "[{}]".format(piece)

        else:
            board[2][square - 7] = "[{}]".format(piece)
    
    # Display the current board state to the user
    for row in board:
        for square in row:
            print(square, end="")
        
        print()
    
    # Bottom margin
    print()


def get_user_move(user_piece, board_state):
    """Given the user's piece and a list of moves already played, 
       get a move from the user, validate that it is legal, and 
       then return the proposed move"""

    while True:
        proposed_move = input("Your move: ")
        move_is_valid = check_move(proposed_move, user_piece, board_state)

        if move_is_valid:
            return proposed_move
        
        else:
            continue


def check_move(proposed_move, user_piece, board_state):
    """Check if a proposed move is legal and return a bool"""

    # Check that user correctly formatted their move
    if len(proposed_move) != 2:
        print("Invalid move! Try again.")
        return False
    
    # Check that user used the correct piece for their move
    elif proposed_move[0] != user_piece:
        print("That is not your piece! Try again.")
        return False

    # Check that the square is empty
    else:
        for move in board_state:
            if proposed_move[1] == move[1]:
                print("There is already a piece there! Try again.")
                return False
        
        return True


def check_board(user_piece, board_state):
    """Check if the game is over and return the result if so"""

    # List containing all possible winning combinations
    possible_wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                     [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    
    # Iterate through all possible winning piece combinations
    for win in possible_wins:
        # Determine if winning combination is present for X
        if check_possible_win("X", win, board_state):
            return determine_result("X", user_piece)
        
        # Determine if winning combination is present for O
        elif check_possible_win("O", win, board_state):
            return determine_result("O", user_piece)
    
    # Determine if game is incomplete (no result and squares still available)
    if len(board_state) != 9:
        return "incomplete"
    
    # If no result and all squares are filled, the result is a draw
    else:
        return "drew"


def check_possible_win(piece, win, board_state):
    """Returns a bool depending on if a win with a 
       given piece is on the board"""
    
    # Check if the given piece has the winning combination on board
    for square in win:
        if "{}{}".format(piece, square) not in board_state:
            return False
        
    return True
        

def determine_result(winning_piece, user_piece):
    """Return result of game depending on what piece the user is"""

    if user_piece == winning_piece:
        return "won"

    else:
        return "lost"


def restart():
    """Ask user if they want to play again and return a bool 
       depending on their answer"""
    
    while True:
        replay_game = input("\nWould you like to play again? (y/n): ")

        if replay_game == "y":
            return True

        elif replay_game == "n":
            return False
