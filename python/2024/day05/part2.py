from itertools import takewhile
from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()
    line_iter = iter(lines)

    ordering = takewhile(lambda x: x != "", line_iter)
    updates = line_iter
    order_map = {}

    for line in ordering:
        dependency, target = map(int, line.split("|"))
        order_map.setdefault(target, []).append(dependency)

    incorrect: list[list[int]] = []

    for update in updates:
        pages = list(map(int, update.split(",")))

        for i, page in enumerate(pages):
            if page not in order_map:
                continue

            if any(dependency in pages[i + 1 :] for dependency in order_map[page]):
                incorrect.append(pages)
                print(pages, page)
                break

    print(incorrect)

    fixed = []

    for update in incorrect:
        ok = False
        while not ok:
            for i, page in enumerate(update):
                if page not in order_map:
                    continue

                for dependency in order_map[page]:
                    try:
                        index = update.index(dependency, i + 1)
                    except ValueError:
                        continue

                    update[i], update[index] = update[index], update[i]
                    break
                else:
                    continue

                break

            else:
                ok = True

        fixed.append(update)

    print(fixed)

    print_output(sum(update[len(update) // 2] for update in fixed))
