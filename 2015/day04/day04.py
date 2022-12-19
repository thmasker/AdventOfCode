from hashlib import md5


def find_lowest_n(zeroes: int) -> int:
    n, start = 0, ''.join(['0' for _ in range(zeroes)])
    while md5(('yzbqklnj' + str(n)).encode('utf-8')).hexdigest()[:zeroes] != start:
        n += 1
    return n


if __name__ == '__main__':
    print(f'Part 1: {find_lowest_n(5)}')
    print(f'Part 2: {find_lowest_n(6)}')
