from itertools import islice

from src.Board import Board


def next_n_lines(opened_file, n):
    opened_file.readline()
    return [line.split() for line in islice(opened_file, n)]


boards = []
complete_board = None
called_number = None

with open("../input/day4.txt") as file:
    numbers = file.readline()[:-1].rsplit(',')

    while board_numbers := next_n_lines(file, 5):
        boards.append(Board(board_numbers))

for number in numbers:
    called_number = int(number)

    for board in boards:
        board.check_number(number)

        if board.is_row_complete() or board.is_column_complete():
            complete_board = board
            print(called_number * complete_board.sum_unmarked_numbers())
            exit(0)
