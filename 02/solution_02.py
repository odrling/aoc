#!/usr/bin/env python3
from dataclasses import dataclass

from open_input import get_input

input_str = get_input(__file__)


cmd_type = list[tuple[str, int]]
commands = [(c, int(v))
            for c, v in (l.split(' ') for l in input_str.splitlines())]


@dataclass
class Boat:
    depth: int = 0
    horizontal_position: int = 0
    aim: int = 0

    def result(self) -> int:
        return self.depth * self.horizontal_position

    def down(self, val: int, aim: bool = False):
        if aim:
            self.aim += val
        else:
            self.depth += val

    def up(self, val: int, aim: bool = False):
        if aim:
            self.aim -= val
        else:
            self.depth -= val

    def forward(self, val: int, aim: bool = False):
        self.horizontal_position += val
        if aim:
            self.depth += (self.aim * val)


def apply_commands(commands: cmd_type, aim: bool = False) -> Boat:
    boat = Boat()
    cmd_handler = {
        'up': boat.up,
        'down': boat.down,
        'forward': boat.forward
    }
    for cmd, val in commands:
        handler = cmd_handler[cmd]
        handler(val, aim)

    return boat


b1 = apply_commands(commands)
print("part 1:", b1.result())

b2 = apply_commands(commands, aim=True)
print("part 2:", b2.result())
