from typing import Callable

STEPS = 25


def solve(print: Callable, print_output: Callable) -> None:
    stones = list(map(int, open(0).read().strip().split()))

    for _ in range(STEPS):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(s := str(stone)) % 2 == 0:
                half = len(s) // 2
                new_stones.extend((int(s[:half]), int(s[half:])))
            else:
                new_stones.append(stone * 2024)

        stones = new_stones

    print_output(len(stones))
