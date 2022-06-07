"""
Exercise No. 86

Given a 3x3 matrix of a completed tic-tac-toe game, create a function that returns whether the game is a win for "X",
"O", or a "Draw", where "X" and "O" represent themselves on the matrix, and "E" represents an empty spot.

Examples:
    tic_tac_toe([
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "X"]
    ]) -> "X"

    tic_tac_toe([
        ["O", "O", "O"],
        ["O", "X", "X"],
        ["E", "X", "X"]
    ]) -> "O"

    tic_tac_toe([
        ["X", "X", "O"],
        ["O", "O", "X"],
        ["X", "X", "O"]
    ]) -> "Draw"

Notes:
    - Make sure that if O wins, you return the letter "O" and not the integer 0 (zero) and if it's a draw, make sure you
    return the capitalized word "Draw". If you return "X" or "O", make sure they're capitalized too.
"""


def tic_tac_toe(board):
    rows = [set(i) for i in board]
    cols = [set(i) for i in zip(*board)]
    diag = [set(board[i][i] for i in range(3)), set(board[i][i] for i in range(-1, -4, -1))]

    for i in rows + cols + diag:
        if len(i) == 1 and "E" not in i:
            return i.pop()
    return "Draw"


print(tic_tac_toe([
        ["X", "X", "O"],
        ["O", "O", "X"],
        ["X", "X", "O"]
    ]))
