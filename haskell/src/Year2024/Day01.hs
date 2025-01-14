module Year2024.Day01 (partOne, partTwo) where

import Data.Function (on)
import Data.List (sort)
import Util

parse :: String -> Either String [(Int, Int)]
parse = mapM parseLine . lines

parseLine :: String -> Either String (Int, Int)
parseLine line = do
  case filter (not . null) $ split ' ' line of
    [l, r] -> (,) <$> readInt l <*> readInt r
    _ -> Left $ "Failed to parse " <> line

partOne :: String -> Either String String
partOne input = do
  inputs <- parse input
  let (left, right) = uncurry ((,) `on` sort) $ unzip inputs
  Right $ show $ sum $ zipWith (fmap abs . (-)) left right

partTwo :: String -> Either String String
partTwo input = do
  inputs <- parse input
  let (left, right) = unzip inputs
  Right $ show $ sum $ map (\n -> n * length (filter (== n) right)) left
