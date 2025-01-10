from collections import defaultdict
from typing import Callable
import graphviz

# code is only helper, the solutions was obtained manually from the graph


def solve(print: Callable, print_output: Callable) -> None:
    lines = iter(open(0).read().splitlines())

    dot = graphviz.Digraph()

    wires = {}

    for line in lines:
        if line == "":
            break

        name, value = line.split(": ")

        wires[name] = bool(int(value))

        dot.node(name, f"{name} = {value}")

    dependencies = defaultdict(list)
    prerequisites = defaultdict(set)

    gates = {}

    for line in lines:
        gate, dst = line.split(" -> ")

        a, gate_type, b = gate.split(" ")

        changes = {
            "fkp": "z06",
            "z06": "fkp",
            "mfm": "z31",
            "z31": "mfm",
            "ngr": "z11",
            "z11": "ngr",
            "bpt": "krj",
            "krj": "bpt",
        }
        if dst in changes:
            dst = changes[dst]

        dependencies[dst].extend([a, b])

        prerequisites[a].add(dst)
        prerequisites[b].add(dst)

        gates[dst] = gate_type

        dot.node(dst, f"{dst} = {gate_type}({a}, {b})")

        dot.edge(a, dst)
        dot.edge(b, dst)

    # dot.render("graph.gv", view=True)

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

    x = sum(
        value << int(wire[1:])
        for wire, value in sorted(wires.items())
        if wire.startswith("x")
    )

    y = sum(
        value << int(wire[1:])
        for wire, value in sorted(wires.items())
        if wire.startswith("y")
    )

    z = sum(
        value << int(wire[1:])
        for wire, value in sorted(wires.items())
        if wire.startswith("z")
    )

    print(f"x = {x}")
    print(f"y = {y}")
    print(f"z = {z}")
    print(f"x + y = {x + y} = {z}")
