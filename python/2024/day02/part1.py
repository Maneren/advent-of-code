from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()
    print(lines)

    unsafe = 0

    for line in lines:
        numbers = list(map(int, line.split(" ")))
        direction = None
        for number, prev in zip(numbers[1:], numbers):
            diff = number - prev
            if not 0 < abs(diff) <= 3:
                unsafe += 1
                break

            c_dir = 1 if diff > 0 else -1

            if direction is None:
                direction = c_dir
                continue

            if direction != c_dir:
                unsafe += 1
                break

    print_output(len(lines) - unsafe)
