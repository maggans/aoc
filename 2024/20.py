from aoc_utils import *

sx,sy = find2d(l,"S")
ex,ey = find2d(l,"E")
shortest = 0
dists = {}
q = deque([(0,ex,ey,(-1,-1))])
while q:
	dist,x,y,prev = q.popleft()
	dists[(x,y)] = dist
	if x == sx and y == sy:
		shortest = dist
		break

	for dx,dy in DIRS:
		cx = x+dx
		cy = y+dy
		if l[cy][cx] != "#" and (cx,cy) != prev:
			q.append((dist+1,cx,cy,(x,y)))

def solve(secs):
	cheats = set()
	cond = shortest - 100
	for (x,y),dist in dists.items():
		distFromStart = shortest - dist
		for i,j in product(range(0,secs+1),repeat=2):
			mh = i + j
			if mh == 0 or mh > secs:
				continue
			
			for dx,dy in [(-i,-j),(-i,j),(i,-j),(i,j)]:
				cx = x+dx
				cy = y+dy
				if (cx,cy) in dists and dists[(cx,cy)] + mh + distFromStart <= cond:
					cheats.add((x,y,cx,cy))
	return len(cheats)

print("Part 1:",solve(2))
print("Part 2:",solve(20))
