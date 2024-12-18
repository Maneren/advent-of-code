from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()
    print(lines)

    right = []
    left = []

    for line in lines:
        r, l = map(int, line.split('   '))
        right.append(r)
        left.append(l)

    right.sort()
    left.sort()

    total = 0
    for r, l in zip(right, left):
        total += abs(r - l)

    # print(total)
    print_output(total)
