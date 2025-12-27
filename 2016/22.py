from aoc_utils import *

resp1 = resp2 = 0
nodes = {}
sx = sy = 0
ex = ey = 0
for line in l[2:]:
	x,y,size,used,avail,_ = ints(line)
	nodes[(x,y)] = [size,used,avail]
	ex = max(ex,x)
	if used == 0:
		sx,sy = x,y
	
for n1,n2 in combinations(nodes,2):
	resp1 += nodes[n1][1] and nodes[n1][1] <= nodes[n2][2]
	resp1 += nodes[n2][1] and nodes[n2][1] <= nodes[n1][2]

sz = nodes[(sx,sy)][0]
vis = set()
q = deque([((sx,sy),(ex,ey),0)])
while q:
	cur,goal,dist = q.popleft()
	if goal == (0,0):
		resp2 = dist
		break
	
	if (cur,goal) in vis:
		continue
	vis.add((cur,goal))
	
	for dx,dy in DIRS:
		next = (cur[0]+dx,cur[1]+dy)
		if next in nodes and nodes[next][1] <= sz:
			if next == goal:
				q.append((next,cur,dist+1))
			else:
				q.append((next,goal,dist+1))

print("Part 1:", resp1)
print("Part 2:", resp2)


