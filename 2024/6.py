from aoc_utils import *

res = 0

sx = sy = 0
g = {}
for i in range(len(l)):
	for j in range(len(l[0])):
		g[(j,i)] = l[i][j]
		if l[i][j] == "^":
			sx,sy = j,i
dirs = {"n":(0,-1,"e"),"s":(0,1,"w"),"w":(-1,0,"n"),"e":(1,0,"s")}
			
def testloop(vis = None):
	dir = "n"
	vis2 = set()
	cx,cy = sx,sy
	dx,dy,nd = dirs[dir]
	while True:
		if vis != None:
			vis.add((cx,cy))
		if (cx,cy,dir) in vis2:
			return 1
		vis2.add((cx,cy,dir))
		if (cx+dx,cy+dy) not in g:
			return 0
		if g[(cx+dx,cy+dy)] == "#":
			dir = nd
			dx,dy,nd = dirs[dir]
		else:
			cx+=dx
			cy+=dy

path = set()
testloop(path)
print("Part 1:",len(path))

for it in path:
	g[it] = "#"
	res+=testloop()
	g[it] = "."
print("Part 2:",res)
