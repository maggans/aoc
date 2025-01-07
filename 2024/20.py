from aoc_utils import *

h = len(l)
w = len(l[0])

g = {}
sx,sy = 0,0
ex,ey = 0,0
for i in range(1,h-1):
	for j in range(1,w-1):
		if l[i][j] == "S":
			sx,sy=j,i
			g[(j,i)] = "."
		elif l[i][j] == "E":
			ex,ey=j,i
			g[(j,i)] = "."
		else:
			g[(j,i)] = l[i][j]

q = deque()
q.append((0,ex,ey))
vis = {}
shortest = 0
dists = {}
while q:
	dist,x,y = q.popleft()
	if x == sx and y == sy:
		shortest = dist
		break
	
	if (x,y) in vis:
		continue
	vis[(x,y)] = 1
	dists[(x,y)] = dist
	
	dd = [(1,0),(-1,0),(0,-1),(0,1)]
	for dx,dy in dd:
		cx = x+dx
		cy = y+dy
		if (cx,cy) in g and g[(cx,cy)] == ".":
			q.append((dist+1,cx,cy))

def getDist(xx,yy):
	if (xx,yy) in dists:
		return dists[(xx,yy)]
	qq = deque()
	qq.append((0,xx,yy))
	v = {}
	
	while qq:
		dist,x,y = qq.popleft()
		
		if dist >= shortest:
			return 99999999
			
		if x == ex and y == ey:
			dists[(xx,yy)] = dist
			return dist

		if (x,y) in v:
			continue
		v[(x,y)] = 1
		dd = [(1,0),(-1,0),(0,-1),(0,1)]
		for dx,dy in dd:
			cx = x+dx
			cy = y+dy
			if (cx,cy) in g and g[(cx,cy)] == ".":
				qq.append((dist+1,cx,cy))
	return 999999999			

lim = 100
if useExample:
	lim = 50

def solve(secs):
	vis = {}
	q = deque()
	q.append((0,sx,sy))
	ss = set()

	cond = shortest - lim
	while q:
		dist,x,y = q.popleft()
		if (x,y) in vis:
			continue
		vis[(x,y)] = 1
		
		if dist > cond:
			continue
		if x == ex and y == ey:
			break

		for i in range(0,secs+1):
			for j in range(0,secs+1):
				mh = i + j
				if mh == 0:
					continue
				
				if mh > secs:
					continue
					
				cord = (x-i,y-j)
				cord2 = (x+i,y+j)
				cord3 = (x+i,y-j)
				cord4 = (x-i,y+j)
				
				ccc = [cord,cord2,cord3,cord4]
				for it in ccc:
					if it in g and g[it] == ".":
						dc = getDist(it[0],it[1])
						dc1 = dc + mh
						if dist+dc1 <= cond:
							ss.add((x,y,it[0],it[1]))
		
		dd = [(1,0),(-1,0),(0,-1),(0,1)]
		for dx,dy in dd:
			cx = x+dx
			cy = y+dy
			if (cx,cy) in g and g[(cx,cy)] == ".":
				q.append((dist+1,cx,cy))
	return len(ss)

print("Part 1:",solve(2))
print("Part 2:",solve(20))
