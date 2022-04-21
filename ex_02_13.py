# 02.13 | 64 | a list with three references the same list is useless

weird_board = [[' '] * 3] * 3
weird_board[1][2] = 'X'

for board_row in weird_board:
    print(board_row)
