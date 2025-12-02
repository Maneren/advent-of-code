from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read()

    id_ranges = (map(int, num.split("-")) for num in map(str.strip, lines.split(",")))

    total = 0

    for start, end in id_ranges:
        for x in range(start, end + 1):
            string = str(x)
            half = len(string) // 2

            if string[:half] == string[half:]:
                total += x

    print_output(total)
