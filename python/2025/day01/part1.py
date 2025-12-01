from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    inputs = open(0).read().splitlines()

    total = 50
    counter = 0

    for line in inputs:
        d, n = line[0], line[1:]
        n = int(n)

        sgn = -1 if d == "L" else 1

        total  = (total + sgn * n + 100 ) % 100

        if total == 0:
            print("adding one")
            counter += 1

        print(d, n, total, counter)

    print(total, counter)
    print_output(counter)


