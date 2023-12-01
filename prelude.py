import sys
import runpy
from datetime import datetime

file = sys.argv[1]

if len(sys.argv) > 2:
    silent = sys.argv[2] == "q"
else:
    silent = False

python_print = print


def empty_print(*a, **kw):
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
