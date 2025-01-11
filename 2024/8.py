from aoc_utils import *

h = len(l)
w = len(l[0])
nodesp1 = set()
nodes = set()
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
		
		nodes.add((x1,y1))
		nodes.add((x2,y2))
		
		added = True
		p1Done = False
		while added:
			added = False
			for xx,yy in [(ax,ay),(ax2,ay2)]:
				if 0 <= xx < w and 0 <= yy < h:
					nodes.add((xx,yy))
					added = True
					if not p1Done:
						nodesp1.add((xx,yy))
			p1Done = True
				
			ax-=xd
			ay-=yd
			ax2+=xd
			ay2+=yd

print("Part 1:",len(nodesp1))
print("Part 2:",len(nodes))
