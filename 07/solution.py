#!/usr/bin/env python3
from collections import Counter

from answer import Answer
from open_input import get_input

input_str = get_input(__file__)
answer = Answer()

crabs: Counter[int] = Counter(map(int, input_str.split(',')))


def sum2n(n: int) -> int:
    return ((n+1)*n) // 2


solutions1 = {target_position: sum(abs(initial_position - target_position) * n
                                   for initial_position, n in crabs.items())
              for target_position in range(max(crabs.keys()))}

solutions2 = {target_position: sum(sum2n(abs(initial_position - target_position)) * n
                                   for initial_position, n in crabs.items())
              for target_position in range(max(crabs.keys()))}

answer.part1 = min(solutions1.values())

answer.part2 = min(solutions2.values())

print(answer)
