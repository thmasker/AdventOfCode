gamma = ''
epsilon = ''

with open("../input/day3.txt") as file:
    lines = file.read().splitlines()
    line_chars = [list(line) for line in lines]

    for col in range(len(line_chars[0])):
        ones = 0
        zeros = 0

        for chars in line_chars:
            if chars[col] == '0':
                zeros += 1
            elif chars[col] == '1':
                ones += 1

        if ones > zeros:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

print(int(gamma, 2) * int(epsilon, 2))
