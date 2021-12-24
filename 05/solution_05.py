#!/usr/bin/env python3
import re

import numpy as np
import toolz
from answer import Answer
from open_input import get_input

input_str = get_input(__file__)
answer = Answer()

line_prog = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')
lines = [tuple(toolz.partition(2, map(int, match_.groups())))
         for match_ in line_prog.finditer(input_str)]


maxn = max(toolz.concat(toolz.concat(lines))) + 1

grid = np.zeros((maxn, maxn))
grid_diag = np.zeros((maxn, maxn))


for start, end in lines:
    minx, maxx = (start[0], end[0]) if start[0] < end[0] else (end[0], start[0])
    miny, maxy = (start[1], end[1]) if start[1] < end[1] else (end[1], start[1])

    if minx == maxx:
        x = minx
        for y in range(miny, maxy + 1):
            grid[x, y] += 1

    elif miny == maxy:
        y = miny
        for x in range(minx, maxx + 1):
            grid[x, y] += 1

    else:  # diagonal line
        stepx = 1 if start[0] < end[0] else -1
        stepy = 1 if start[1] < end[1] else -1

        for x, y in zip(range(start[0], end[0] + stepx, stepx),
                        range(start[1], end[1] + stepy, stepy)):
            grid_diag[x, y] += 1


grid2 = grid + grid_diag

answer.part1 = np.count_nonzero(grid > 1)
answer.part2 = np.count_nonzero(grid2 > 1)

print(answer)
