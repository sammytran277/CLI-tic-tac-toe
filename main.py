from main_game_loop import game_loop, show_board, get_user_move


def intro():
    """Display ASCII art at the start of the game"""

    print(r"""
     _   _         _                _             
    | | (_)       | |              | |            
    | |_ _  ___   | |_ __ _  ___   | |_ ___   ___ 
    | __| |/ __   | __/ _` |/ __   | __/ _ \ / _ \
    | |_| | (__   | || (_| | (__   | || (_) |  __/
    \__|_|\___|   \__\__,_|\___|   \__\___/ \___|

    """)


def choose_piece():
    """Return the user's chosen piece"""

    print("Please select a piece! X goes first and O goes second: ", end="")

    while True:
        piece = input()

        if piece != "X" and piece != "O":
            print("Please choose either X or O: ", end="")

        else:
            return piece


if __name__ == "__main__":
    while True:
        intro()
        user_piece = choose_piece()
        replay_game = game_loop(user_piece)

        # Exit loop if user doesn't want to play again
        if not replay_game:
            break


