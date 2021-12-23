#!/usr/bin/env python3
from open_input import get_input
import toolz

input_str: str = get_input(__file__)


depth_readings = list(map(int, input_str.splitlines(keepends=False)))


def count_increases(depth_readings: list[int]):
    count = 0
    for d1, d2 in zip(depth_readings, depth_readings[1:]):
        if d2 > d1:
            count += 1

    return count


def group_entries(depth_readings: list[int]):
    return [sum(w) for w in toolz.sliding_window(3, depth_readings)]


print("part 1:", count_increases(depth_readings))
print("part 2:", count_increases(group_entries(depth_readings)))
