from typing import Callable


def mix(value, secret):
    return value ^ secret


def prune(secret):
    return secret % 16777216


def next_number(secret):
    value = secret * 64
    secret = mix(value, secret)
    secret = prune(secret)

    value = secret // 32
    secret = mix(value, secret)
    secret = prune(secret)

    value = secret * 2048
    secret = mix(value, secret)
    secret = prune(secret)

    return secret


def solve(print: Callable, print_output: Callable) -> None:
    lines = map(int, open(0).read().splitlines())

    total = 0

    for number in lines:
        secret = number
        for _ in range(2000):
            secret = next_number(secret)
        total += secret

    print_output(total)
