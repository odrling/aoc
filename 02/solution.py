#!/usr/bin/env python3
from open_input import get_input
from dataclasses import dataclass

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


def apply_commands(commands: cmd_type, aim: bool = False) -> Boat:
    boat = Boat()
    for cmd, val in commands:
        match cmd:
            case "down":
                if aim:
                    boat.aim += val
                else:
                    boat.depth += val
            case "up":
                if aim:
                    boat.aim -= val
                else:
                    boat.depth -= val
            case "forward":
                boat.horizontal_position += val
                if aim:
                    boat.depth += (boat.aim * val)

    return boat


b1 = apply_commands(commands)
print("part 1:", b1.result())

b2 = apply_commands(commands, aim=True)
print("part 2:", b2.result())

