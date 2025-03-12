from itertools import islice


def window(seq, n=3):
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


increased_measures = 0

with open("../input/day1.txt") as file:
    lines = [int(x) for x in file.readlines()]

    current_sum = 0
    for sector in window(lines):
        first_sector = sum(sector)

        if first_sector > current_sum:
            increased_measures += 1
        current_sum = first_sector

increased_measures -= 1
print(increased_measures)
