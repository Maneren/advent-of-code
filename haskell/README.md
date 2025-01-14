# Haskell

Structure and tooling based on <https://github.com/Blugatroff/adventofcode>,
thanks a lot.

## How to Run

```sh
cabal run aoc -- 2022 17 two
```

## Architecture

The solution to every day is in its own module and exports two functions, one for either part of the problem.

Both functions always have the same signature.

```haskell
partOne :: String -> Either String String
partTwo :: String -> Either String String
```

The [Main](https://github.com/Blugatroff/adventofcode/blob/main/src/Main.hs)
module then just has to pick the right function from the list of days, depending
on the CLI arguments, and apply it to the input.

## Static musl executable, because it's neat

```sh
docker build -t aoc . && docker run --rm -v $(pwd):/app aoc
```
