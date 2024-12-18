from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()
    print(lines)

    right = []
    left = []

    for line in lines:
        l, r = map(int, line.split("   "))
        right.append(r)
        left.append(l)

    occurences = {}

    for r in right:
        if r in occurences:
            occurences[r] += 1
        else:
            occurences[r] = 1

    total = sum(l * occurences[l] for l in left if l in occurences)

    print_output(total)
