from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = list(map(list, open(0).read().splitlines()))

    start = next(
        (x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "S"
    )

    print(start)

    splits = 0

    for line, next_line in zip(lines[start[1] :], lines[start[1] + 1 :]):
        print(line, next_line, sep="\n")
        for i, (c, nc) in enumerate(zip(line, next_line)):
            if c == "S":
                next_line[i] = "|"

            if c == "|":
                if nc == "^":
                    splits += 1
                    for di in (-1, 1):
                        try:
                            next_line[i + di] = "|"
                        except IndexError:
                            pass
                elif nc == ".":
                    next_line[i] = "|"

        print(line, next_line, sep="\n")
        print()

    print(*lines, sep="\n")

    print_output(splits)
