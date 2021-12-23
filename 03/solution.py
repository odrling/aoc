#!/usr/bin/env python3
from collections import Counter

from open_input import get_input

input_str = get_input(__file__)

readings: list[int] = [int(v, base=2) for v in input_str.splitlines()]
readings_len = len(input_str.splitlines(keepends=False)[0])


def get_count(readings: list[int], readings_len: int) -> list[Counter[bool]]:
    counter: list[Counter[bool]] = [Counter() for _ in range(readings_len)]
    for v in readings:
        for i in range(readings_len):
            counter[i].update([v & (1 << i) > 0])

    return counter


def get_gamma(counter: list[Counter[bool]]) -> int:
    counter = get_count(readings, readings_len)

    return sum((1 << i) for i in range(readings_len)
               if counter[i].most_common(1)[0][0])


def get_epsilon(counter: list[Counter[bool]]) -> int:
    counter = get_count(readings, readings_len)

    return sum((1 << i) for i in range(readings_len)
               if not counter[i].most_common(1)[0][0])


def get_oxygen_rating(readings: list[int], readings_len: int) -> int:
    pos = readings_len - 1
    while len(readings) > 1:
        counter = Counter((r & (1 << pos)) > 0 for r in readings)
        if counter[True] >= counter[False]:
            readings = [v for v in readings if (v & (1 << pos)) > 0]
        else:
            readings = [v for v in readings if (v & (1 << pos)) == 0]

        pos -= 1

    return readings[0]


def get_co2_rating(readings: list[int], readings_len: int) -> int:
    pos = readings_len - 1
    while len(readings) > 1:
        counter = Counter((r & (1 << pos)) > 0 for r in readings)
        if counter[True] < counter[False]:
            readings = [v for v in readings if (v & (1 << pos)) > 0]
        else:
            readings = [v for v in readings if (v & (1 << pos)) == 0]

        pos -= 1

    return readings[0]


counter = get_count(readings, readings_len)
gamma = get_gamma(counter)
epsilon = get_epsilon(counter)

print("part 1:", gamma * epsilon)

oxygen_rating = get_oxygen_rating(readings, readings_len)
co2_rating = get_co2_rating(readings, readings_len)
print("part 2:", co2_rating * oxygen_rating)
