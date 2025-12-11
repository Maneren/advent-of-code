import re
from typing import Callable

import numpy as np
from scipy.optimize import linprog


def apply(current: tuple[int, ...], button: int | tuple[int, ...]) -> tuple[int, ...]:
    current_list = list(current)

    for i in button:
        current_list[i] += 1

    return tuple(current_list)


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).readlines()

    parsed = [
        (
            tuple(map(int, re.search(r"\{(.*)\}", line).expand(r"\1").split(","))),
            [
                tuple(map(int, button.split(",")))
                for button in re.findall(r"\((\d++(?:,\d++)*)\)", line)
            ],
        )
        for line in lines
    ]

    total = 0

    for target, buttons in parsed:
        vectors = [apply(tuple(0 for _ in target), button) for button in buttons]

        a_eq = np.stack(vectors, axis=1, dtype=np.int64)
        b_eq = np.array(target, dtype=np.int64)
        c = np.ones(len(vectors), dtype=np.int64)
        result = linprog(c, A_eq=a_eq, b_eq=b_eq, integrality=1)

        if result.success:
            total += round(result.fun)

    print_output(total)
