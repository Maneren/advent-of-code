import functools
from typing import Callable

def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()
    patterns = tuple(lines[0].split(", "))

    @functools.cache
    def construct_pattern(desired, current) -> bool:
        return any(
            (test := current + pattern) == desired
            or desired.startswith(test)
            and construct_pattern(desired, test)
            for pattern in patterns
        )

    print_output(sum(construct_pattern(patt, "") for patt in lines[2:]))
