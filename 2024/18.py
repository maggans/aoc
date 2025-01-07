from aoc_utils import *

sx, sy = 0,0
ex,ey = 70,70
if useExample:
	ex,ey=6,6

g = {}
for i,line in enumerate(l):
	if i == 1024:
		break
	x,y = ints(line)
	g[(x,y)] = "#"
	# print(x,y)
	
for i in range(71):
	for j in range(71):
		if (j,i) not in g:
			g[(j,i)] = "."

def bfs():
	q = deque()
	q.append((0,sx,sy))
	vis = {}
	while q:
		d,nx,ny = q.popleft()
		# print(nx,ny)
		if nx == ex and ny == ey:
			return d
		
		if (nx,ny) in vis:
			continue
		vis[(nx,ny)] = 1
		
		dd = [(-1,0),(1,0),(0,-1),(0,1)]
		for dx,dy in dd:
			cx = nx+dx
			cy = ny+dy
			if (cx,cy) in g and g[(cx,cy)] == ".":
				q.append((d+1,cx,cy))
	return -1

print("Part 1:", bfs())
	
for i in range(1024,len(l)):
	x,y = ints(l[i])
	g[(x,y)] = "#"
	
	if bfs() == -1:
		print("Part 2:", str(x) + "," + str(y))
		break
