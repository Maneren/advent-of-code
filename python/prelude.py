import sys
import runpy
from datetime import datetime

file = sys.argv[1]
silent = sys.argv[2] == "q" if len(sys.argv) > 2 else False

python_print = print


def empty_print(*_a, **_kw):
    pass


def print_output(*a, **kw):
    python_print(*a, **kw)


def print(*a, **kw):
    python_print(*a, **kw, file=sys.stderr)


print_fn = empty_print if silent else print

solve_function = runpy.run_path(file)["solve"]

start = datetime.now()
solve_function(print_fn, print_output)
end = datetime.now()

runtime = end - start
print("Executed in: ", runtime)
