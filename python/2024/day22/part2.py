from collections import defaultdict
from itertools import pairwise
import itertools
from typing import Callable

def next_number(secret):
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216

    return secret

def sliding_window(iterable, n=2):
    iterables = itertools.tee(iterable, n)

    for iterable, num_skipped in zip(iterables, itertools.count()):
        for _ in range(num_skipped):
            next(iterable, None)

    return zip(*iterables)

def solve(print: Callable, print_output: Callable) -> None:
    lines = map(int, open(0).read().splitlines())

    sequence_values = defaultdict(int)

    for number in lines:
        secret_numbers = [
            number % 10,
            *((number := next_number(number)) % 10 for _ in range(2000)),
        ]

        differences = (
            next_secret - secret for secret, next_secret in pairwise(secret_numbers)
        )

        seen = set()
        for n, sequence in zip(secret_numbers[4:], sliding_window(differences, 4)):
            if sequence not in seen:
                sequence_values[sequence] += n
                seen.add(sequence)

    print_output(max(sequence_values.values()))
