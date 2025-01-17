from aoc_utils import *

sx,sy = find2d(l,"S")
ex,ey = find2d(l,"E")
q = [(0,sx,sy,0,[])]
vis = {}
paths = {(sx,sy)}
bestScore = None
dirs = [(1,0),(0,1),(-1,0),(0,-1)]
while q:
	score,x,y,dir,path = heapq.heappop(q)
	if x == ex and y == ey:
		if bestScore is None or score == bestScore:
			bestScore = score
			paths |= set(path)
		continue
	
	if (x,y,dir) in vis and vis[(x,y,dir)] != score:
			continue
	vis[(x,y,dir)] = score
	
	dx,dy = dirs[dir]
	if l[y+dy][x+dx] != "#":
		heapq.heappush(q,(score+1,x+dx,y+dy,dir,path+[(x+dx,y+dy)]))
	heapq.heappush(q,(score+1000,x,y,(dir+1)%4,path))
	heapq.heappush(q,(score+1000,x,y,(dir+3)%4,path))

print("Part 1:", bestScore)
print("Part 2:", len(paths))
