use y2023_day_06::*;

fn main() {
    divan::main();
}

const INPUT: &'static str = include_str!("../input.txt");

#[divan::bench]
fn part1() {
    part1::solve(divan::black_box(INPUT)).unwrap();
}

#[divan::bench]
fn part2() {
    part2::solve(divan::black_box(INPUT)).unwrap();
}
