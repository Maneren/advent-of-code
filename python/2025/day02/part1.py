from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    id_ranges = [
        tuple(map(int, num.split("-"))) for line in lines for num in
        line.split(",") if num
    ]

    total = 0

    for start, end in id_ranges:
        for x in range(start, end + 1):
            string = str(x)

            half = len(string) // 2

            if string[:half] == string[half:]:
                print(x)
                total += x


    print(total)
    print_output(total)

    
