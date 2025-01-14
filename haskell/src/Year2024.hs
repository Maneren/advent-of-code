module Year2024 (year) where

import Data.Map qualified as M
import Day (Day (Day), Year (Year))
import Year2024.Day01 qualified as Day01

days :: M.Map Int Day
days =
  M.fromList
    [ (1, Day Day01.partOne Day01.partTwo)
    ]

year :: Year
year = Year 2024 days
