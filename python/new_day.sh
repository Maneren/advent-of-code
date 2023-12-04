#!/bin/env bash

main() {
    printf -v day '%(%d)T' -1
    printf -v year '%(%Y)T' -1
    part='1'


    if [[ "$1" = 'y'* ]]; then
        year="20${1#y}"
        shift
    fi

    if [[ "$1" = 'd'* ]]; then
        day="${1#d}"
        shift
    fi

    if [[ ${#day} = 1 ]]; then
        day="0${day}"
    fi

    day_with_no_zero="${day#0}"

    folder="$year/day${day}"
    python_file1="$folder/part1.py"
    python_file2="$folder/part2.py"
    input_file="$folder/input.txt"
    sample_file="$folder/sample.txt"
    output_file="$folder/output.txt"

    if [ -d "$folder" ]; then
        echo "Day $day of year $year already exists"
        exit 1
    fi

    echo "Creating day $day of year $year, part $part"

    local default_py=$'def solve(print, print_output):\n    lines = open(0).read().splitlines()'

    mkdir "$folder"
    echo "" >"$sample_file"
    echo "" >"$output_file"
    echo "$default_py" >"$python_file1"
    echo "$default_py" >"$python_file2"


    if [[ -z $AOC_COOKIE ]]; then
        echo "Trying to load AOC_COOKIE from .env"
        source .env

        if [[ -z $AOC_COOKIE ]]; then
            echo "AOC_COOKIE not set"
            exit 1
        fi
    fi

    curl --cookie "session=$AOC_COOKIE" -sS "https://adventofcode.com/$year/day/$day_with_no_zero/input" >"$input_file"
}

main "$@"
