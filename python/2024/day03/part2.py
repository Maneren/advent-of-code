from typing import Callable
import re

re.finditer


def solve(print: Callable, print_output: Callable) -> None:
    i = open(0).read()

    dos = [(m.start(), True) for m in re.finditer(r"do\(\)", i)]
    donts = [(m.start(), False) for m in re.finditer(r"don't\(\)", i)]
    switches = sorted(dos + donts)
    switch_i = 0

    enabled = True

    total = 0
    regex = re.compile(r"mul\((\d+),(\d+)\)")
    for m in regex.finditer(i):
        if m.start() >= switches[switch_i][0] and switch_i < len(switches) - 1:
            enabled = switches[switch_i][1]
            switch_i += 1

        if enabled:
            total += int(m.group(1)) * int(m.group(2))

    print_output(total)
