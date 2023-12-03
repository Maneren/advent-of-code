from typing import Generator


def neighbors_iter(
    lines: list[str], x: int, y: int, length
) -> Generator[str, None, None]:
    for i in range(x - 1, x + length + 1):
        for j in range(y - 1, y + 2):
            if 0 <= i < len(lines) and 0 <= j < len(lines[0]):
                yield lines[j][i]


def load_number(line: list[str], x: int) -> tuple[int, int]:
    length = 0
    number = 0
    while x < len(line) and line[x].isdigit():
        length += 1
        number *= 10
        number += int(line[x])
        x += 1

    return length, number


def solve(print, print_output):
    lines = open(0).read().splitlines()

    sum_of_part_numbers = 0

    for y, line in enumerate(lines):
        x = 0
        while x < len(line):
            if not line[x].isdigit():
                continue

            length, number = load_number(line, x)
            if any(
                not (neighbor.isdigit() or neighbor == ".")
                for neighbor in neighbors_iter(lines, x, y, length)
            ):
                sum_of_part_numbers += number
                x += length - 1

            x += 1

    print_output(sum_of_part_numbers)
