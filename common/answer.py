from dataclasses import dataclass


@dataclass
class Answer:
    part1: int | None = None
    part2: int | None = None

    def __str__(self):
        answers = []
        if self.part1 is not None:
            answers.append(f"part 1: {self.part1}")
        if self.part2 is not None:
            answers.append(f"part 2: {self.part2}")

        return "\n".join(answers)
