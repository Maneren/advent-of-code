from queue import PriorityQueue
import re
from typing import Callable


def apply(current: tuple[bool, ...], button: tuple[int, ...]) -> tuple[bool, ...]:
    current_list = list(current)

    for i in button:
        current_list[i] = not current_list[i]

    return tuple(current_list)


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).readlines()

    parsed = [
        (
            list(re.match(r"\[(.*)\]", line).expand(r"\1")),
            [
                tuple(map(int, button.split(",")))
                for button in map(str.strip, re.findall(r"\((\d++(?:,\d++)*)\)", line))
            ],
        )
        for line in lines
    ]

    total = 0

    for target, buttons in parsed:
        target = tuple(light == "#" for light in target)

        visited = set()

        queue = PriorityQueue()
        queue.put((0, tuple(False for _ in target)))

        while queue:
            steps, current = queue.get()

            if current == target:
                total += steps
                break

            for button in buttons:
                new = apply(current, button)

                if new in visited:
                    continue

                visited.add(new)

                queue.put((steps + 1, new))

    print_output(total)
