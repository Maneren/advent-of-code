from typing import Generator, Callable

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

directions = [UP, RIGHT, DOWN, LEFT]

directions_map = {
    (UP, "F"): RIGHT,
    (LEFT, "F"): DOWN,
    (DOWN, "L"): RIGHT,
    (LEFT, "L"): UP,
    (UP, "7"): LEFT,
    (RIGHT, "7"): DOWN,
    (DOWN, "J"): LEFT,
    (RIGHT, "J"): UP,
    (UP, "|"): UP,
    (DOWN, "|"): DOWN,
    (LEFT, "-"): LEFT,
    (RIGHT, "-"): RIGHT,
}


def use_direction(
    position: tuple[int, int], direction: tuple[int, int]
) -> tuple[int, int]:
    return position[0] + direction[0], position[1] + direction[1]


def next_in_path(
    map: list[str], current_pos: tuple[int, int], direction: tuple[int, int]
) -> tuple[int, int]:
    x, y = current_pos

    next_char = map[y][x]

    return directions_map[direction, next_char]


def s_neighbors(
    map: list[str], position: tuple[int, int]
) -> Generator[tuple[int, int], None, None]:
    x, y = position
    for direction in directions:
        nx, ny = x + direction[0], y + direction[1]
        try:
            type = map[ny][nx]
        except IndexError:
            continue

        try:
            __test_direction = directions_map[direction, type]
        except KeyError:
            continue

        if type == ".":
            continue

        yield direction


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    # find the S
    for i, line in enumerate(lines):
        try:
            s_position = line.index("S"), i
        except ValueError:
            continue

    direction, _ = s_neighbors(lines, s_position)

    position = use_direction(s_position, direction)

    i = 1
    while position != s_position:
        direction = next_in_path(lines, position, direction)
        position = use_direction(position, direction)
        i += 1

    print_output(i // 2)
