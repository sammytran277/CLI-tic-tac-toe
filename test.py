from game_loop import check_board
from move_generation import threaten_win


# ["X1", "O2", "O3", "O4", "X5", "O6", "X7", "O8", "X9"]
# ["X1", "X2", "X3", "[ ]", "O5", "[ ]", "O7", "[ ]", "O9"]
# ["X1", "O2", "X3", "O4", "O5", "X6", "X7", "X8", "O9"]
# ["O1", "X2", "X3", "X4", "O5", "X6", "[ ]", "X8", "O9"]
# ["[ ]", "[ ]", "X3", "[ ]", "O5", "[ ]", "[ ]", "[ ]", "[ ]"]

tests = [["X1", "O2", "O3", "O4", "X5", "O6", "X7", "O8", "X9"],
         ["X1", "X2", "X3", "[ ]", "O5", "[ ]", "O7", "[ ]", "O9"],
         ["X1", "O2", "X3", "O4", "O5", "X6", "X7", "X8", "O9"],
         ["O1", "X2", "X3", "X4", "O5", "X6", "[ ]", "X8", "O9"],
         ["[ ]", "[ ]", "X3", "[ ]", "O5", "[ ]", "[ ]", "[ ]", "[ ]"]]

# for test in tests:
#     result = check_board("O", test)
#     print(result)


