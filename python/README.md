# Advent of Code

This folder contains my tooling and primary solutions for the Advent of Code
challenges.

It is written in Bash for Python and requires `curl` for communication with the
AoC server.

## Tooling

All arguments are optional and must be used in the same order they are listed
here.

All scripts are assumed to be run form the root folder (same as this file) and
that the environment variable `AOC_COOKIE` is either set, or can be sourced
from a `.env` file in the same folder.

```bash
AOC_COOKIE=abcdef123456789....
```

## `new_day.sh`

Creates a template for a new challenge and download the test input. Without any
arguments it will choose today's challenge. Possible arguments are `y<year` and
`d<day>`, picking the year and day respectively.

> [!note] Sample input is not downloaded automatically.

## `solve.sh`

This runs the solution for the specifies challenge and optionally submits the
result. By default, it will again choose today's challenge. Possible arguments
are also `y<year>` and `d<day>` for picking the year and day, `p<part>` for
picking either the first or second part, `sample` for using the sample input
instead of the test input, `q` for suppressing the output to console and `send`
for submitting the result to AOC.

Examples:

```sh
./solve.sh y23 d01 sample # solve day 1 of 2023, sample input
./solve.sh d11            # solve day 11 of this year, part 1
./solve.sh p2 q send      # solve today's part 2, suppress output and submit
```

## `prelude.py`

Sets up the environment and defined few helper functions for IO. Gets called
by the `solve.sh` script and in turn calls the specified challenge solution.

> [!important]
> For this to work the solution must be a single file script containing the `solve`
> function, that takes in two parameters: `print` and `print_output`. `print` is
> for the debug output, `print_output` is for the final output that gets submitted.

`print` outputs to stderr and `print_output` to stdout, in order to work nicely
with shell's output capturing.
