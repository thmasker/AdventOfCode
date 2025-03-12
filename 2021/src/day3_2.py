import functools
import operator


def find_oxygen(line_chars):
    oxygen_lines = line_chars

    for col in range(len(oxygen_lines[0])):
        ones = 0
        zeros = 0

        for chars in oxygen_lines:
            if chars[col] == '0':
                zeros += 1
            elif chars[col] == '1':
                ones += 1

        if ones >= zeros:
            oxygen_lines = [line for line in oxygen_lines if line[col] == '1']
        else:
            oxygen_lines = [line for line in oxygen_lines if line[col] == '0']

    return functools.reduce(operator.iconcat, oxygen_lines, [])


def find_co2(line_chars):
    co2_lines = line_chars

    for col in range(len(co2_lines[0])):
        ones = 0
        zeros = 0

        for chars in co2_lines:
            if chars[col] == '0':
                zeros += 1
            elif chars[col] == '1':
                ones += 1

        if ones < zeros:
            co2_lines = [line for line in co2_lines if line[col] == '1']
        else:
            co2_lines = [line for line in co2_lines if line[col] == '0']

        if len(co2_lines) == 1:
            break

    return functools.reduce(operator.iconcat, co2_lines, [])


oxygen = ''
co2 = ''

oxygen_lines = []
co2_lines = []

with open("../input/day3.txt") as file:
    lines = file.read().splitlines()
    line_chars = [list(line) for line in lines]

    oxygen_lines = find_oxygen(line_chars)
    co2_lines = find_co2(line_chars)

print(int(oxygen.join(oxygen_lines), 2) * int(co2.join(co2_lines), 2))
