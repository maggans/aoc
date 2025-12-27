from aoc_utils import *

pos = (0,0)
dir = NORTH
vis = {pos}
resp2 = None
for it in l[0].split(", "):
	if it[0] == "R":
		dir = turnRight(dir)
	else:
		dir = turnLeft(dir)
	for i in range(int(it[1:])):
		pos = tuple(map(operator.add, pos, DIRS[dir]))
		if pos in vis and resp2 is None:
			resp2 = abs(pos[0]) + abs(pos[1])
		vis.add(pos)

print("Part 1:", abs(pos[0]) + abs(pos[1]))
print("Part 2:", resp2)
