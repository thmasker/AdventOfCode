def find_start_of_packet_marker(marker_length: int) -> int:
    line = open('input.txt', 'r').readline()
    for i in range(len(line)):
        if len(set(line[i: i + marker_length])) == marker_length:
            return i + marker_length


if __name__ == '__main__':
    print(f'Part 1: {find_start_of_packet_marker(4)}')
    print(f'Part 2: {find_start_of_packet_marker(14)}')
