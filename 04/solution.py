#!/usr/bin/env python3
import re

import toolz
from answer import Answer
from open_input import get_input

input_str: str = get_input(__file__)
answer = Answer()

num_prog = re.compile(r'\d+')

drawables: list[int] = list(map(int, input_str.splitlines()[0].split(',')))

boards_nums = map(int, num_prog.findall("\n".join(input_str.splitlines()[1:])))


class Board:

    def __init__(self, board_nums: tuple[int]):
        self.board: tuple[tuple[int, ...], ...] = tuple(toolz.partition(5, board_nums))

    def check_against(self, drawn: set[int]) -> bool:
        for x in self.board:
            if len(set(x) - drawn) == 0:
                return True

        for x in zip(*self.board):
            if len(set(x) - drawn) == 0:
                return True

        return False

    def result(self, drawn: set[int], last_num: int) -> int:
        remaining = set(toolz.concat(self.board)) - drawn
        return sum(remaining) * last_num


boards = [Board(board_nums)
          for board_nums in toolz.partition(25, boards_nums)]


def bingo_loop(last: bool = False):
    local_boards = boards.copy()
    drawn = set()
    last_board_result: int | None = None

    for i in drawables:
        drawn.add(i)
        to_remove = []

        for board_n, board in enumerate(local_boards):
            if board.check_against(drawn):
                last_board_result = board.result(drawn, i)
                if last:
                    to_remove.append(board_n)
                else:
                    return last_board_result

        for n in reversed(to_remove):
            del local_boards[n]

    if last_board_result is None:
        raise RuntimeError("Game never ends")

    return last_board_result


answer.part1 = bingo_loop()
answer.part2 = bingo_loop(last=True)


print(answer)
