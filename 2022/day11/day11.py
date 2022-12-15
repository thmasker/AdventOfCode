from __future__ import annotations

import math
import operator


class Monkey:
    def __init__(self, items: list[int], operation: str, divisible: int, true: int, false: int):
        self.items = items
        self.operator = operator.mul if operation[0] == '*' else operator.add
        self.operand = operation[2:]
        self.divisible = divisible
        self.true = true
        self.false = false
        self.inspections = 0

    def perform_operation(self, item: int) -> int:
        return self.operator(item, item if self.operand == 'old' else int(self.operand))

    def process_turn(self, monkeys: list[Monkey], lcm: int, divide_by: int = 1):
        while self.items:
            self.inspections += 1
            item = self.operator(self.items[0], self.items[0] if self.operand == 'old' else int(self.operand))
            item %= lcm
            item //= divide_by
            if item % self.divisible == 0:
                monkeys[self.true].items.append(item)
            else:
                monkeys[self.false].items.append(item)
            self.items.pop(0)


def get_monkeys_info(rounds: int, divide_by: int = 1) -> int:
    monkeys_unparsed = open('input.txt').read().split('\n\n')
    monkeys = []
    for monkey in monkeys_unparsed:
        monkey = [line.strip() for line in monkey.split('\n')]
        items = [int(item) for item in monkey[1][16:].split(', ')]
        operation = monkey[2][21:]
        divisible = int(monkey[3][19:])
        true = int(monkey[4][25:])
        false = int(monkey[5][25:])
        monkeys.append(Monkey(items, operation, divisible, true, false))

    lcm = math.lcm(*[monkey.divisible for monkey in monkeys])
    for _ in range(rounds):
        for monkey in monkeys:
            monkey.process_turn(monkeys, lcm, divide_by)

    monkeys.sort(key=lambda x: x.inspections, reverse=True)
    return monkeys[0].inspections * monkeys[1].inspections


if __name__ == '__main__':
    print(f'Part 1: {get_monkeys_info(20, 3)}')
    print(f'Part 2: {get_monkeys_info(10_000)}')
