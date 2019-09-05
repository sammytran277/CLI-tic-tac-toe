"""This is the main file of the game which uses all the other 
   modules' functions to create a command line Tic-Tac-Toe game!"""

from game_loop import game_loop


def main():
    while True:
        intro()
        user_piece = choose_piece()

        if user_piece == "X":
            computer_piece = "O"

        else:
            computer_piece = "X"

        replay_game = game_loop(user_piece, computer_piece)

        # Exit loop if user doesn't want to play again
        if not replay_game:
            break


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
    main()


