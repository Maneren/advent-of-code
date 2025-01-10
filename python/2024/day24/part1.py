from collections import defaultdict
from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = iter(open(0).read().splitlines())

    wires = {}

    for line in lines:
        if line == "":
            break

        name, value = line.split(": ")

        wires[name] = bool(int(value))

    prerequisites = defaultdict(set)
    dependencies = {}

    gates = {}

    for line in lines:
        gate, dst = line.split(" -> ")

        a, gate_type, b = gate.split(" ")

        dependencies[dst] = [a, b]

        prerequisites[a].add(dst)
        prerequisites[b].add(dst)

        gates[dst] = gate_type

    while dependencies:
        evaluated = tuple(wires.keys())

        for wire in evaluated:
            for dst in tuple(prerequisites[wire]):
                other = next(dep for dep in dependencies[dst] if dep != wire)
                if other not in wires:
                    continue

                gate_type = gates[dst]

                if gate_type == "AND":
                    wires[dst] = wires[wire] and wires[other]
                elif gate_type == "OR":
                    wires[dst] = wires[wire] or wires[other]
                elif gate_type == "XOR":
                    wires[dst] = wires[wire] != wires[other]
                else:
                    raise ValueError

                del dependencies[dst]
                prerequisites[wire].remove(dst)
                prerequisites[other].remove(dst)

    number = sum(
        value << int(wire[1:])
        for wire, value in sorted(wires.items())
        if wire.startswith("z")
    )

    print_output(number)
