from aoc_utils import *

floors = [1 if c == "(" else -1 for c in l[0]]
print("Part 1:", sum(floors))
print("Part 2:", list(accumulate(floors)).index(-1) + 1)
