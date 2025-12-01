from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    inputs = open(0).read().splitlines()

    total = 50
    counter = 0

    for line in inputs:
        d, n = line[0], line[1:]
        n = int(n)


        while d == "L" and total - n <= 0:
            n -= 100
            counter += 1

        if d == "L" and total == 0:
            counter -= 1

        while d == "R" and total + n >= 100:
            n -= 100
            counter += 1

        change = -n if d == "L" else n
        total  = (total + change + 100) % 100

    print(total, counter)
    print_output(counter)


