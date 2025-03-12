class Board:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_row_complete(self):
        return any(all(n == 'x' for n in row) for row in self.numbers)

    def is_column_complete(self):
        return any(all(n == 'x' for n in row) for row in self.__transpose())

    def check_number(self, number):
        for row in self.numbers:
            for i in range(len(row)):
                if number == row[i]:
                    row[i] = 'x'
                    return

    def sum_unmarked_numbers(self):
        return sum([int(n) for row in self.numbers for n in row if n != 'x'])

    def __transpose(self):
        rows = len(self.numbers)
        cols = len(self.numbers[0])

        matrix_t = []
        for j in range(cols):
            row = []
            for i in range(rows):
                row.append(self.numbers[i][j])
            matrix_t.append(row)

        return matrix_t
