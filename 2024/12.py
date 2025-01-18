from aoc_utils import *

gard = {}
for i in range(len(l)):
	for j in range(len(l[i])):
		gard[(j,i)] = l[i][j]

resp1 = resp2 = 0
vis = set()
for k,v in gard.items():
	if k in vis:
		continue

	group = set()
	q = deque([k])
	while q:
		x,y = q.popleft()
		if (x,y) in vis:
			continue
		vis.add((x,y))
		group.add((x,y))
		for dx,dy in DIRS:
			cx = x+dx
			cy = y+dy
			if (cx,cy) in gard and gard[(cx,cy)] == v:
				q.append((cx,cy))

	perimeter = 0
	area = len(group)
	fence = set()	
	for x,y in group:
		perimeter += 4
		for dir,(dx,dy) in enumerate(DIRS):
			cx = x+dx
			cy = y+dy
			if (cx,cy) in group:
				perimeter-=1
			else:
				fence.add((cx,cy,dir))
		
	sides = 0
	fvis = set()
	for x,y,dir in fence:		
		if (x,y,dir) in fvis:
			continue
		sides+=1
		dx = dir is NORTH or dir is SOUTH 
		dy = dir is WEST or dir is EAST
		for sign in [1,-1]:
			cx = x+sign*dx
			cy = y+sign*dy
			while (cx,cy,dir) in fence:
				fvis.add((cx,cy,dir))
				cx+=sign*dx
				cy+=sign*dy
	
	resp1+=area*perimeter
	resp2+=area*sides

print("Part 1:",resp1)
print("Part 2:",resp2)
