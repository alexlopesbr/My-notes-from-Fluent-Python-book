# 02.12 | 64 | A list with three size 3 lists can represent an tic-tac-toe board

board = [[' '] * 3 for i in range(3)]

board[1][2] = 'X'
board[0][0] = 'O'

for board_row in board:
    print(board_row)
