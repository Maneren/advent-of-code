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
        if [[ -z $AOC_COOKIE ]]; then
            echo "Trying to load AOC_COOKIE from .env"
            source .env

            if [[ -z $AOC_COOKIE ]]; then
                echo "AOC_COOKIE not set"
                exit 1
            fi
        fi

        curl -sS --cookie "session=$AOC_COOKIE" \
            "https://adventofcode.com/$year/day/$day_with_no_zero/answer" \
            --data "level=$part&answer=$output" \
            | pup 'article > p text{}' \
            | perl -CS -MHTML::Entities -ne 'print decode_entities($_)' \
            | head -n -1 \
            | head -c -1 \
            | tr '\n' ' ' \
            | sed 's/\([[:space:]]\)\+/\1/g' \
            | sed 's/ \([[:punct:]]\)/\1/g'

    fi
}

main "$@"
