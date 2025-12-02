import re
from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read()

    invalid_id = re.compile(r"^(\d+)\1++$")

    total = sum(
        x
        for num in map(str.strip, lines.split(","))
        for x in range(*map(int, num.split("-")))
        if invalid_id.match(str(x))
    )

    print_output(total)
