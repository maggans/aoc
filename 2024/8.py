from aoc_utils import *

res = 0

h = len(l)
w = len(l[0])

nodesp1 = {}
nodes = {}
ant = defaultdict(list)

for y in range(h):
	for x in range(w):
		if l[y][x].isalnum():
			ant[l[y][x]].append((x,y))

for v in ant.values():
	for a,b in combinations(v,2):
		x1,y1 = a
		x2,y2 = b
		
		xd = x2-x1
		yd = y2-y1
		
		ax = x1-xd
		ay = y1-yd
		
		ax2 = x2+xd
		ay2 = y2+yd
		
		nodes[x1,y1] = 1
		nodes[x2,y2] = 1
		
		added = True
		p1Done = False
		while added:
			added = False
			if 0 <= ax < w and 0 <= ay < h:
				nodes[(ax,ay)] = 1
				added = True
				if not p1Done:
					nodesp1[(ax,ay)] = 1
			if 0 <= ax2 < w and 0 <= ay2 < h:
				nodes[(ax2,ay2)] = 1
				added = True
				if not p1Done:
					nodesp1[(ax2,ay2)] = 1
			p1Done = True
				
			ax = ax-xd
			ax2 = ax2+xd
			ay = ay-yd
			ay2 = ay2+yd

print("Part 1:",len(nodesp1))
print("Part 2:",len(nodes))
