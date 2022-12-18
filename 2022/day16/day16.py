import re
from dataclasses import dataclass, field

Tunnel = tuple[int, int]
Tunnels = set[Tunnel]
MinimumDistance = dict[int, dict[int, int]]


@dataclass
class Valve:
    flow_rate: int
    valves: set[int] = field(default_factory=set)


Valves = dict[int, Valve]


def get_valves() -> Valves:
    lines = open('input2.txt').readlines()

    valves = {}
    valve_n = 0
    names_mapping = {}
    for line in lines:
        flow_rate = int(re.search(r'\d+', line).group())
        valves[valve_n] = Valve(flow_rate)
        names_mapping[re.findall('[A-Z][A-Z]', line)[0]] = valve_n
        valve_n += 1

    for line in lines:
        names = re.findall('[A-Z][A-Z]', line)
        for name in names[1:]:
            valves[names_mapping[names[0]]].valves.add(names_mapping[name])

    return valves


def get_tunnels(valves: Valves) -> Tunnels:
    tunnels = set()
    for key, start_valve in valves.items():
        for end_valve in start_valve.valves:
            tunnels.add((key, end_valve))
    return tunnels


def floyd_warshall(valves: Valves, tunnels: Tunnels) -> MinimumDistance:
    dist = {valve: {valve: float('inf') for valve in valves} for valve in valves}

    for u, v in tunnels:
        dist[u][v] = 1

    for name, valve in valves.items():
        dist[name][name] = 0

    for k in valves:
        for i in valves:
            for j in valves:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def get_useful_valves(valves: Valves) -> Valves:
    useful_valves = {}
    for name, valve in valves.items():
        if valve.flow_rate > 0:
            useful_valves[name] = valve
    return useful_valves


def get_maximum_pressure(valves: Valves, current_valve: int, useful_valves: Valves, distances: MinimumDistance,
                         opened_valves: str, computed: dict[int, dict[str, int]], time: int = 30) -> int:
    if opened_valves in computed[time]:
        return computed[time][opened_valves]

    max_pressure = 0
    for name, valve in useful_valves.items():
        if opened_valves[name] == '0':
            new_time = time - distances[current_valve][name] - 1
            if new_time > 0:  # todo a lo mejor >=
                new_pressure = valve.flow_rate * new_time
                new_opened_valves = opened_valves[:name] + '1' + opened_valves[name + 1:]
                max_pressure = max(max_pressure,
                                   new_pressure + get_maximum_pressure(valves, name, useful_valves, distances,
                                                                       new_opened_valves, computed, new_time))

    computed[time][opened_valves] = max_pressure
    return max_pressure


def part1() -> int:
    valves = get_valves()
    distances = floyd_warshall(valves, get_tunnels(valves))
    useful_valves = get_useful_valves(valves)
    return get_maximum_pressure(valves, 0, useful_valves, distances, ''.join(['0' for _ in range(len(valves))]),
                                {time: {} for time in range(1, 31)})


def part2() -> int:
    pass


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    # print(f'Part 2: {part2()}')
