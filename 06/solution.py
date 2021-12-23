#!/usr/bin/env python3
from collections import Counter

from answer import Answer
from open_input import get_input

input_str = get_input(__file__)
answer = Answer()

init_timers = list(map(int, input_str.split(',')))


def lanternfish_loop(init_timers: list[int], days: int) -> int:
    lanternfishs = {i: 0 for i in range(9)}
    lanternfishs.update(Counter(init_timers))

    for _ in range(days):
        new_lanternfishs = lanternfishs[0]
        for i in range(1, 9):
            lanternfishs[i-1] = lanternfishs[i]

        lanternfishs[8] = new_lanternfishs
        lanternfishs[6] += new_lanternfishs

    return sum(lanternfishs.values())


answer.part1 = lanternfish_loop(init_timers, 80)
answer.part2 = lanternfish_loop(init_timers, 256)

print(answer)
