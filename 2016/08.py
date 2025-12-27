from aoc_utils import *

g = [deque(["."] * 50) for _ in range(6)]
for it in l:
	a,b = ints(it)
	if it.startswith("rect"):
		for i in range(b):
			for j in range(a):
				g[i][j] = "#"
	elif it.startswith("rotate row"):
		g[a].rotate(b)
	else:
		for _ in range(b):
			prev = g[-1][a]
			for i in range(6):
				prev,g[i][a] = g[i][a],prev
	
print("Part 1:", sum(row.count("#") for row in g))
print("Part 2:\n" + "\n".join("".join(row) for row in g))
