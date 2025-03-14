# https://github.com/MaxMaxoff/AdventOfCode2021/blob/master/Day6_Lanternfish/Day6_Lanternfish.py

def calculate_grow(initial_state, days):
    new_state = {}

    if days > 0:
        for i in [1, 2, 3, 4, 5, 6, 7, 8, 0]:
            if i == 0 and initial_state.get(i):
                new_state[8] = initial_state[i]
                if new_state.get(6):
                    new_state[6] += initial_state[i]
                else:
                    new_state[6] = initial_state[i]
            elif i > 0 and initial_state.get(i):
                new_state[i - 1] = initial_state[i]

        return calculate_grow(new_state, days - 1)

    return initial_state


def main(days):
    initial_state = {}
    result_state = {}

    with open("../input/day6.txt") as file:
        initial_list = list(map(int, file.readline().split(',')))

    for item in initial_list:
        if initial_state.get(item):
            initial_state[item] += 1
        else:
            initial_state[item] = 1

    qty = 0
    result_state = calculate_grow(initial_state, days)

    for key in result_state:
        qty += result_state[key]

    print(qty)


if __name__ == "__main__":
    main(256)
