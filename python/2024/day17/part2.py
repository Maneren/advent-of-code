from itertools import takewhile
from typing import Callable


def eval(program, A, B, C):
    a = A
    b = B
    c = C
    result = []
    IP = 0

    while IP + 1 < len(program):
        COMBO = [0, 1, 2, 3, a, b, c]

        operand = program[IP + 1]
        match program[IP]:
            case 0:
                a >>= COMBO[operand]
            case 1:
                b ^= operand
            case 2:
                b = COMBO[operand] & 7
            case 3:
                IP = operand - 2 if a else IP
            case 4:
                b ^= c
            case 5:
                result.append(COMBO[operand] & 7)
            case 6:
                b = a >> COMBO[operand]
            case 7:
                c = a >> COMBO[operand]

        IP += 2

    return result


def dfs(program, A, B, C, i):
    result = eval(program, A, B, C)

    if result == program:
        return A

    if i != 0 and result != program[-i:]:
        return None

    for n in range(8):
        if (output := dfs(program, A * 8 + n, B, C, i + 1)) is not None:
            return output

    return None


def solve(print: Callable, print_output: Callable) -> None:
    lines = iter(open(0).read().splitlines())

    _, B, C = (int(line.split(": ")[1]) for line in takewhile(lambda x: x != "", lines))

    program = list(map(int, "".join(lines).split(": ")[1].split(",")))

    print_output(dfs(program, 0, B, C, 0))
