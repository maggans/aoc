from aoc_utils import *

resp1 = resp2 = None
sx,sy = find2d(l,"0")
locations = sum([c.isdigit() for row in l for c in row])
q = deque([(0,sx,sy,("0",))])
cache = set()
while q:
	dist,x,y,vis = q.popleft()
	if len(vis) == locations:
		if not resp1:
			resp1 = dist
		if (x,y) == (sx,sy):
			resp2 = dist
			break

	if (x,y,vis) in cache:
		continue
	cache.add((x,y,vis))
	
	for dx,dy in DIRS:
		nx,ny = x+dx,y+dy
		if l[ny][nx] == "." or l[ny][nx] in vis:
			q.append((dist+1,nx,ny,vis))
		elif l[ny][nx] != "#":
			q.append((dist+1,nx,ny,vis + (l[ny][nx],)))	

print("Part 1:", resp1)
print("Part 2:", resp2)
