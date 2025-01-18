from aoc_utils import *

g = {}
starts = []
for i in range(len(l)):
	for j in range(len(l[i])):
		g[(j,i)] = int(l[i][j])
		if l[i][j] == "0":
			starts.append((j,i,0))
	
def solve(p1=False):
	ans = 0
	for it in starts:
		q = deque([it])
		vis = set()
		while q:
			x,y,d = q.popleft()
			
			if p1 and (x,y) in vis:
				continue
			vis.add((x,y))
			
			if d == 9:
				ans+=1
				continue

			for dx,dy in DIRS:
				cx = x+dx
				cy = y+dy
				if (cx,cy) in g and g[(cx,cy)] == d+1:
					q.append((cx,cy,d+1))
	return ans
				
print("Part 1:",solve(True))
print("Part 2:",solve(False))
