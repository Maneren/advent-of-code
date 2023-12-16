use std::{ops::Index, time::Instant};

use itertools::Itertools;
use rustc_hash::FxHashMap;

#[allow(dead_code)]
fn main() -> Result<(), String> {
    let start = Instant::now();
    let result = solve(include_str!("../input.txt")).map_err(|e| e.to_string())?;
    let elapsed = start.elapsed();
    println!("'{}' in {elapsed:?}", result.to_string());
    Ok(())
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
enum Direction {
    Right = 0,
    Left = 1,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
struct Mapping<'a> {
    left: &'a str,
    right: &'a str,
}

impl<'a> Index<Direction> for Mapping<'a> {
    type Output = &'a str;
    fn index(&self, index: Direction) -> &Self::Output {
        match index {
            Direction::Right => &self.right,
            Direction::Left => &self.left,
        }
    }
}

pub fn solve(input: &str) -> Result<impl ToString, String> {
    let lines = input.lines().map(|line| line.trim()).collect::<Vec<&str>>();

    let directions = lines[0]
        .chars()
        .map(|c| match c {
            'R' => Direction::Right,
            'L' => Direction::Left,
            _ => unreachable!(),
        })
        .cycle();

    let mappings = lines[2..]
        .into_iter()
        .map(|line| {
            let (from, to) = line
                .split_once(" = ")
                .ok_or_else(|| format!("Invalid mapping line: {line}"))?;

            let (left, right) = to[1..to.len() - 1]
                .split_once(", ")
                .ok_or_else(|| format!("Invalid mapping: {to}"))?;

            let to = Mapping { left, right };

            Ok((from, to))
        })
        .collect::<Result<FxHashMap<_, _>, String>>()?;

    let (steps, _) = directions
        .scan("AAA", |state, direction| {
            *state = mappings.get(*state)?[direction];
            Some(*state)
        })
        .find_position(|state| *state == "ZZZ")
        .ok_or_else(|| format!("ZZZ not found"))?;

    Ok(steps + 1)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> Result<(), String> {
        let input = "RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)";
        let result = solve(input)?.to_string();
        assert_eq!("2", result);
        Ok(())
    }
}
