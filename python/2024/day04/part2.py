from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    total = 0

    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[i]) - 1):
            if lines[i][j] != "A":
                continue

            tl = lines[i - 1][j - 1]
            bl = lines[i + 1][j - 1]
            tr = lines[i - 1][j + 1]
            br = lines[i + 1][j + 1]

            tlr = tl == "M" and br == "S"
            blr = bl == "M" and tr == "S"
            trl = tr == "M" and bl == "S"
            brl = br == "M" and tl == "S"

            if tlr + blr + trl + brl == 2:
                total += 1

    print_output(total)
