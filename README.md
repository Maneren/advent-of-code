# Advent of Code

This repo contains tooling and my solutions for the Advent of Code challenges.

## Tooling

All arguments are optional and must be used in the same order they are listed here.
All scripts are assumed to be run form the root of the repo and that the environment
variable `AOC_COOKIE` is either set, or can be sourced from `.env` file
in the root of the repo.

### `new_day.sh`

Creates a template for a new challenge and download the test input.
Without any arguments it will choose today's challenge. Possible arguments
are `y<year` and `d<day>`, picking the year and day respectively.

## `solve.sh`

This runs the solution for the specifies challenge and optionally submits the result.
By default, it will again choose today's challenge. Possible arguments are
also `y<year>` and `d<day>` for picking the year and day, `p<part>` for picking
either the first or second part, `sample` for using the sample input instead of
the test input, `q` for suppressing the output to console and `send` for submitting
the result to AOC.

## `prelude.py`

Sets up the environment and defined few helper functions for IO. Gets called
by the `solve.sh` script and in turn calls the specified challenge solution.
For this to work the solution must be a single file script containing the `solve`
function, that takes in two parameters: `print` and `print_output`. `print`
counterintuitively outputs to stderr and `print_output` to stdout,
in order to work properly with shell's output capturing.
