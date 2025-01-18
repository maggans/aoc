from aoc_utils import *

sx,sy = find2d(l,"^")
g = {}
for i in range(len(l)):
	for j in range(len(l[0])):
		g[(j,i)] = l[i][j]

def testloop(vis = None):
	dir = NORTH
	vis2 = set()
	cx,cy = sx,sy
	dx,dy = DIRS[dir]
	while True:
		if vis != None:
			vis.add((cx,cy))
		if (cx,cy,dir) in vis2:
			return 1
		vis2.add((cx,cy,dir))
		if (cx+dx,cy+dy) not in g:
			return 0
		if g[(cx+dx,cy+dy)] == "#":
			dir = turnRight(dir)
			dx,dy = DIRS[dir]
		else:
			cx+=dx
			cy+=dy

path = set()
testloop(path)
print("Part 1:",len(path))

resp2 = 0
for it in path:
	g[it] = "#"
	resp2 += testloop()
	g[it] = "."
print("Part 2:",resp2)
