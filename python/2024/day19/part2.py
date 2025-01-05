import functools
from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()
    patterns = tuple(lines[0].split(", "))

    @functools.cache
    def contruct_pattern(desired, current) -> int:
        return sum(
            (test := current + pattern) == desired
            or desired.startswith(test)
            and contruct_pattern(desired, test)
            for pattern in patterns
        )

    total = sum(contruct_pattern(patt, "") for patt in lines[2:])
    print_output(total)
