from typing import Generator


def neighbors_iter(
    lines: list[str], x: int, y: int
) -> Generator[tuple[int, int, str], None, None]:
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if 0 <= i < len(lines) and 0 <= j < len(lines[0]):
                yield i, j, lines[j][i]


def load_number(line: list[str], x: int) -> int:
    number = 0

    while x > 0 and line[x - 1].isdigit():
        x -= 1

    while x < len(line) and line[x].isdigit():
        number *= 10
        number += int(line[x])
        x += 1

    return number


def solve(print, print_output):
    lines = open(0).read().splitlines()

    sum_of_gear_ratios = 0

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != "*":
                continue

            numbers = []
            for i, j, c in neighbors_iter(lines, x, y):
                if not c.isdigit():
                    continue
                number = load_number(lines[j], i)
                if number not in numbers:
                    numbers.append(number)

            if len(numbers) == 2:
                print(numbers)
                sum_of_gear_ratios += numbers[0] * numbers[1]

    print_output(sum_of_gear_ratios)
