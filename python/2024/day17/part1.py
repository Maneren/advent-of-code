from itertools import takewhile
from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = iter(open(0).read().splitlines())

    a, b, c = (int(line.split(": ")[1]) for line in takewhile(lambda x: x != "", lines))

    program = list(map(int, "".join(lines).split(": ")[1].split(",")))

    print(a, b, c)
    print(program)

    IP = 0

    def combo(operand):
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4 | 5 | 6:
                return [a, b, c][operand - 4]
            case _:
                raise ValueError

    output = []

    while IP + 1 < len(program):
        instruction, operand = program[IP : IP + 2]

        IP += 2

        match instruction:
            case 0:
                a //= 2 ** combo(operand)
            case 1:
                b ^= operand
            case 2:
                b = combo(operand) % 8
            case 3:
                if a != 0:
                    IP = operand
            case 4:
                b ^= c
            case 5:
                output.append(combo(operand) % 8)
            case 6:
                b = a // 2 ** combo(operand)
            case 7:
                c = a // 2 ** combo(operand)

    print_output(",".join(map(str, output)))
