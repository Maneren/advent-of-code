from itertools import pairwise
from typing import Callable
from functools import cache

KEYPADS = {
    0 + 0j: "7",
    1 + 0j: "8",
    2 + 0j: "9",
    0 + 1j: "4",
    1 + 1j: "5",
    2 + 1j: "6",
    0 + 2j: "1",
    1 + 2j: "2",
    2 + 2j: "3",
    1 + 3j: "0",
    2 + 3j: "A",
    0 + 4j: "<",
    1 + 4j: "v",
    2 + 4j: ">",
}

BUTTONS = {v: k for k, v in KEYPADS.items()}

def should_reverse(button, next_button):
    return all(
        corner in KEYPADS
        for corner in [
            (next_button.real + button.imag * 1j),
            (button.real + next_button.imag * 1j),
        ]
    )

@cache
def find_button_count(code, remaining_depth) -> int:
    if remaining_depth < 0:
        return len(code) + 1  # press the code and an A

    length = 0
    for char, next_char in pairwise(f"A{code}A"):
        diff = (next_button := BUTTONS[next_char]) - (button := BUTTONS[char])
        real, imag = map(int, (diff.real, diff.imag))
        next_code = ">" * real + "v" * imag + "0" * -imag + "<" * -real

        if should_reverse(button, next_button):
            next_code = next_code[::-1]

        length += find_button_count(next_code, remaining_depth - 1)

    return length

def solve(print: Callable, print_output: Callable) -> None:
    codes = open(0).read().splitlines()

    print_output(
        sum(find_button_count(code[:-1], 25) * int(code[:-1]) for code in codes)
    )
