from aoc_utils import *

resp1 = resp2 = 0
grid = defaultdict(lambda: (0,0))
for it in l:
	x1,y1,x2,y2 = ints(it)
	op = lambda x: (not x[0], x[1]+2)
	if it.startswith("turn on"):
		op = lambda x: (1, x[1]+1)
	elif it.startswith("turn off"):
		op = lambda x: (0, max(x[1]-1,0))
	for x,y in product(range(x1,x2+1),range(y1,y2+1)):
		grid[(x,y)] = op(grid[(x,y)])
for r1,r2 in grid.values():
	resp1 += r1
	resp2 += r2	
print("Part 1:", resp1)
print("Part 2:", resp2)
