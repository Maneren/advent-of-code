# Advent of Code 2023

The solutions here are my attempts at creating as fast solution
as I can as a way to practice optimizing and benchmarking in Rust.

Based on the [Chris Biscardi's repo][chris-repo]. Relevant parts of the original
README:

## Quick setup

```shell
rustup default nightly
cargo install cargo-nextest cargo-generate flamegraph just
```

## Prepare for a new day

```shell
just create <year> <day>
```

## Run the tooling

```shell
just work <year> <day> <part>
```

This is equivalent workflow of running all of these in a row and
stopping if one fails, then re-starting the flow after changes.

```shell
cargo check
cargo nextest run
cargo clippy
cargo bench
cargo flamegraph
```

[chris-repo]: https://github.com/ChristopherBiscardi/advent-of-code
