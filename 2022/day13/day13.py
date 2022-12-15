from functools import reduce

Packet = list[int | list[int]]
PacketPair = tuple[Packet, Packet]


def get_items(packet_str: str) -> list[str]:
    items, item, open_bracket = [], '', 0
    for char in packet_str:
        if char == ',':
            if open_bracket:
                item += char
            else:
                items.append(item)
                item = ''
        elif char == '[':
            open_bracket += 1
            item += char
        elif char == ']':
            open_bracket -= 1
            item += char
        else:
            item += char
    items.append(item)
    return items


def parse_packet(packet_str: str) -> Packet | int:
    if packet_str[0] == '[':
        if len(packet_str) == 2:
            return []
        return [parse_packet(item) for item in get_items(packet_str[1:-1])]
    else:
        return int(packet_str)


def parse_packet_pair(pair: str) -> PacketPair:
    packets = pair.split('\n')
    return parse_packet(packets[0]), parse_packet(packets[1])


def parse_pairs() -> list[PacketPair]:
    packet_pairs = open('input.txt').read().split('\n\n')
    return [parse_packet_pair(pair) for pair in packet_pairs]


def compare_integers(left: int, right: int) -> bool:
    if left < right:
        return True
    elif left > right:
        return False


def is_ordered(left: Packet, right: Packet, i: int = 0) -> bool:
    if i == min(len(left), len(right)):
        return compare_integers(len(left), len(right))

    l, r = left[i], right[i]
    l_int, r_int = isinstance(l, int), isinstance(r, int)

    if l_int and r_int:
        ordered = compare_integers(l, r)
    else:
        l = [l] if l_int else l
        r = [r] if r_int else r

        ordered = is_ordered(l, r)

    if ordered is None:
        return is_ordered(left, right, i + 1)

    return ordered


def merge(left: list[Packet], right: list[Packet]) -> list[Packet]:
    packets = []

    while left and right:
        if is_ordered(left[0], right[0]):
            packets.append(left.pop(0))
        else:
            packets.append(right.pop(0))

    while left:
        packets.append(left.pop(0))
    while right:
        packets.append(right.pop(0))

    return packets


def merge_sort(packets: list[Packet]) -> list[Packet]:
    if len(packets) <= 1:
        return packets

    left, right = [], []
    for i, item in enumerate(packets):
        if i < len(packets) // 2:
            left.append(item)
        else:
            right.append(item)

    left, right = merge_sort(left), merge_sort(right)
    return merge(left, right)


def part1() -> int:
    pairs = parse_pairs()

    indices_sum = 0
    for i, pair in enumerate(pairs):
        if is_ordered(pair[0], pair[1]):
            indices_sum += i + 1

    return indices_sum


def part2() -> int:
    dividers = [[[2]], [[6]]]
    packets = []
    for pair in parse_pairs():
        packets.extend([pair[0], pair[1]])
    packets.extend(dividers)

    packets = merge_sort(packets)

    indices = []
    for i, packet in enumerate(packets):
        if packet in dividers:
            indices.append(i + 1)
    return reduce(lambda x, y: x * y, indices)


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
