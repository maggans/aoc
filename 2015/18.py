from aoc_utils import *

g = [list(x) for x in l]
g2 = [list(x) for x in l]
h = len(g)
w = len(g[0])
corners = [(0,0),(0,w-1),(h-1,0),(h-1,w-1)]
for y,x in corners:
	g2[y][x] = "#"

def solve(g,p1):
	for i in range(100):
		gc = copy.deepcopy(g)
		for y in range(h):
			for x in range(w):
				on = 0
				for dx,dy in DIRSDIAG:
					if 0 <= x+dx < w and 0 <= y+dy < h and g[y+dy][x+dx] == "#":
						on+=1
				if g[y][x] == "#" and on not in [2,3] and (p1 or (y,x) not in corners):
					gc[y][x] = "."
				elif g[y][x] == "." and on == 3:
					gc[y][x] = "#"
		g = gc
	return sum([it.count("#") for it in g])

print("Part 1:", solve(g,True))
print("Part 2:", solve(g2,False))
