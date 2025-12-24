from aoc_utils import *

print("Part 1:", sum([len(s) - len(eval(s)) for s in l]))
print("Part 2:", sum([s.count('\"') + s.count('\\') + 2 for s in l]))
