from aoc_utils import *

def solve(p1):
	vis = set()
	q = deque([(0,1,1)])
	while q:
		steps,x,y = q.popleft()
		
		if p1 and x == 31 and y == 39:
			return steps
		
		if (x,y) in vis or not p1 and steps > 50:
			continue
		vis.add((x,y))
		
		for dx,dy in DIRS:
			nx = x+dx
			ny = y+dy
			t = nx**2 + 3*nx + 2*nx*ny + ny + ny**2 + int(l[0])
			if nx >= 0 and ny >= 0 and binToStr(t).count("1") % 2 == 0:
				q.append((steps+1,nx,ny))
	return len(vis)
	
print("Part 1:", solve(True))
print("Part 2:", solve(False))
