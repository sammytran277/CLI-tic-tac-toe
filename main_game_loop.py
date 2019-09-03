"""This module contains all the functions for the main game loop except for 
   the code that generates the computer's moves"""


def game_loop(user_piece):
    """Main game loop which handles everything from displaying the board, 
       taking a user move, generating a computer response, and checking 
       the board state"""
    
    # Board state contains all the moves played in the game thus far
    board_state = []

    while True:
        show_board(board_state)

        # TODO: Figure out how to determine who goes first

        move = get_user_move(user_piece, board_state)
        board_state.append(move)

        # TODO: Implement check_board
        # TODO: End game loop if the game is over


def show_board(board_state):
    """Given a list of moves in tic-tac-toe notation, show the board"""

    # Top margin
    print()

    # Here, the board is represented as a 2D matrix
    board = [["| |", "| |", "| |"], 
             ["| |", "| |", "| |"], 
             ["| |", "| |", "| |"]]

    # Iterate through all moves in the moves list and add to board
    for move in board_state:
        piece = move[0]
        square = int(move[1])

        if square in [1, 2, 3]:
            board[0][square - 1] = "|{}|".format(piece)

        elif square in [4, 5, 6]:
            board[1][square - 4] = "|{}|".format(piece)

        else:
            board[2][square - 7] = "|{}|".format(piece)
    
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


def check_board(board_state):
    """Check if there is a win on the current board"""

    # TODO


def game_over(result):
    """Congratulate the user for winning or thank them for playing"""

    # TODO: May not be necessary actually, but we will see