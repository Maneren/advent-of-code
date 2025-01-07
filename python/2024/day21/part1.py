from collections import defaultdict
from queue import PriorityQueue
from typing import Callable

KEYPAD = {
    0: "7",
    1: "8",
    2: "9",
    0 + 1j: "4",
    1 + 1j: "5",
    2 + 1j: "6",
    0 + 2j: "1",
    1 + 2j: "2",
    2 + 2j: "3",
    1 + 3j: "0",
    2 + 3j: "A",
}

KEYPAD_BUTTONS = {v: k for k, v in KEYPAD.items()}

DIRECTIONAL_KEYPAD = {
    1: "^",
    2: "A",
    0 + 1j: "<",
    1 + 1j: "v",
    2 + 1j: ">",
}

DIRECTIONAL_BUTTONS = {v: k for k, v in DIRECTIONAL_KEYPAD.items()}

DIRECTIONS = {
    "^": -1j,
    "v": 1j,
    "<": -1,
    ">": 1,
}


def find_path(grid, start, end) -> set[str]:
    paths = set()
    values = defaultdict(lambda: 1e9)
    queue = PriorityQueue()
    queue.put((0, t := 0, start, []))

    best = 1e9

    while not queue.empty():
        value, _, position, path = queue.get()

        if value > values[position]:
            continue

        values[position] = value

        if position == end:
            if value > best:
                break
            best = value
            paths.add(tuple(path))

        for symbol, move in DIRECTIONS.items():
            new_position = position + move

            if new_position not in grid:
                continue

            queue.put(
                (
                    value + 1,
                    t := t + 1,
                    new_position,
                    path + [symbol],
                )
            )

    return paths


def construct_path(code, grid, buttons) -> set[str]:
    paths = set()
    for char, next_char in zip(f"A{code}", code):
        subpaths = find_path(grid, buttons[char], buttons[next_char])
        assert subpaths

        paths = (
            {path + "".join(subpath) + "A" for subpath in subpaths for path in paths}
            if paths
            else {"".join(subpath) + "A" for subpath in subpaths}
        )

    return paths


def solve(print: Callable, print_output: Callable) -> None:
    codes = open(0).read().splitlines()

    total = 0

    for code in codes:
        print(code)
        paths = construct_path(code, KEYPAD, KEYPAD_BUTTONS)
        second_paths = {
            second_path
            for path in paths
            for second_path in construct_path(
                path, DIRECTIONAL_KEYPAD, DIRECTIONAL_BUTTONS
            )
        }
        third_paths = {
            third_path
            for second_path in second_paths
            for third_path in construct_path(
                second_path, DIRECTIONAL_KEYPAD, DIRECTIONAL_BUTTONS
            )
        }
        total += len(min(third_paths, key=len)) * int(code[:-1])

    print_output(total)


# <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
# v<<A>>^A<A>AvA<^AA>A<vAAA>^A
# <A^A>^^AvvvA
# 029A

# 029A
# <A^A>^^AvvvA
# <v<A>>^A<A>AvA<^AA>Av<AAA^>A
# v<A<AA>>^AvAA^<A>Av<<A>^>AvA^A<vA>^A<Av<A>^>AAvA^Av<<A>A^>AAAvA<^A>A
