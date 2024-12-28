from typing import Callable

STEPS = 75

cache = {}


def solve(print: Callable, print_output: Callable) -> None:
    stones_input = list(map(int, open(0).read().strip().split()))

    stones = {}
    for stone in stones_input:
        if stone in stones:
            stones[stone] += 1
        else:
            stones[stone] = 1

    for _ in range(STEPS):
        new_stones = {}
        for stone, count in stones.items():
            if stone == 0:
                new_stones.setdefault(1, 0)
                new_stones[1] += count
            elif (digits := len(str(stone))) % 2 == 0:
                half = digits // 2
                higher, lower = map(int, divmod(stone, 10**half))

                new_stones.setdefault(higher, 0)
                new_stones[higher] += count
                new_stones.setdefault(lower, 0)
                new_stones[lower] += count
            else:
                new_stones.setdefault(stone * 2024, 0)
                new_stones[stone * 2024] += count

        stones = new_stones

    print_output(sum(stones.values()))
