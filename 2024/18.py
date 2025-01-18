from aoc_utils import *

sx,sy = 0,0
ex,ey = 70,70
bytes = set()
for i in range(0,1024):
	bytes.add(tuple(ints(l[i])))

def bfs():
	q = deque([(0,sx,sy)])
	vis = set()
	while q:
		d,x,y = q.popleft()
		if x == ex and y == ey:
			return d
		
		if (x,y) in vis:
			continue
		vis.add((x,y))
		
		for dx,dy in DIRS:
			cx = x+dx
			cy = y+dy
			if sx <= cx <= ex and sy <= cy <= ey and (cx,cy) not in bytes:
				q.append((d+1,cx,cy))
	return -1

print("Part 1:", bfs())
	
for i in range(1024,len(l)):
	bytes.add(tuple(ints(l[i])))
	if bfs() == -1:
		print("Part 2:", l[i])
		break
