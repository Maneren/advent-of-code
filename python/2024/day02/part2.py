from typing import Callable


def check(numbers: list[int]):
    direction = None
    for number, next_ in zip(numbers[1:], numbers):
        diff = next_ - number
        if not 0 < abs(diff) <= 3:
            return False

        direc = 1 if diff > 0 else -1
        if direction is None:
            direction = direc
            continue

        if direction != direc:
            return False

    return True


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    safe = 0

    for line in lines:
        numbers = list(map(int, line.split(" ")))

        if check(numbers):
            safe += 1
            continue

        if any(check(numbers[:i] + numbers[i + 1 :]) for i in range(len(numbers))):
            safe += 1

    print_output(safe)
