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

    if [[ $1 = 'p'* ]]; then
        part="${1#p}"
        shift
    fi

    if [[ ${#day} = 1 ]]; then
        day="0${day}"
    fi

    day_with_no_zero="${day#0}"

    echo "Solving day $day of year $year, part $part"

    folder="$year/day${day}"
    python_file="$folder/part${part}.py"

    if [[ "$1" = 'sample' ]]; then
        input_file="$folder/sample.txt"
        shift
    else
        input_file="$folder/input.txt"
    fi

    output_file="$folder/output.txt"

    output=$(python3 prelude.py "$python_file" "$1" <"$input_file")
    exit_code=$?

    printf '%s' "$output" | xclip -sel clip

    echo "$output" | tee "$output_file"

    if [[ $1 = 'send' && $exit_code = 0 ]]; then
        curl --cookie "session=$AOC_COOKIE" -sS "https://adventofcode.com/$year/day/$day_with_no_zero/answer" --data "level=$part&answer=$output"
    fi
}

main "$@"
