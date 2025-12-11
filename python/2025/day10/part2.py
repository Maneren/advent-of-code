import re
from typing import Callable

import numpy as np
from scipy.optimize import linprog


def apply(current: tuple[int, ...], button: int | tuple[int, ...]) -> tuple[int, ...]:
    current_list = list(current)

    if isinstance(button, int):
        current_list[button] += 1
    else:
        for i in button:
            current_list[i] += 1

    return tuple(current_list)


def heuristic(current: tuple[int, ...], target: tuple[int, ...]) -> int:
    return sum(y - x for x, y in zip(current, target))


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).readlines()

    parsed = [
        (
            tuple(map(int, re.search(r"\{(.*)\}", line).expand(r"\1").split(","))),
            [
                tuple(map(int, x.split(",")))
                for x in re.findall(r"\((\d++(?:,\d++)*)\)", line)
            ],
        )
        for line in lines
    ]

    total = 0

    for target, buttons in parsed:
        vectors = [apply(tuple(0 for _ in target), button) for button in buttons]

        print(target)
        print(vectors)

        A_eq = np.stack(vectors).T
        b_eq = np.array(target)
        c = np.ones(len(vectors))
        print(A_eq.shape, b_eq.shape, c.shape)
        result = linprog(c, A_eq=A_eq, b_eq=b_eq, integrality=1)

        print(result.x, result.fun)

        if result.success:
            total += round(result.fun)

    print_output(total)
