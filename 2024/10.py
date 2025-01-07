from aoc_utils import *

h = len(l)
w = len(l[0])
# print(h,w)
res = 0

g = {}
starts = []

for i in range(h):
	for j in range(w):
		g[(j,i)] = int(l[i][j])
		if int(l[i][j]) == 0:
			starts.append((j,i,0))
	
def solve(p1=False):
	ans = 0
	for it in starts:
		q = deque()
		q.append(it)
		vis = {}
		while q:
			x,y,d = q.popleft()
			
			if p1 and (x,y) in vis:
				continue
			vis[(x,y)] = 1
			
			if d == 9:
				assert g[(x,y)] == 9
				ans+=1
				continue

			dd = [(-1,0),(1,0),(0,-1),(0,1)]
			for dx,dy in dd:
				cx = x+dx
				cy = y+dy
				if (cx,cy) in g and g[(cx,cy)] == d+1:
					q.append((cx,cy,d+1))
	return ans
				
print("Part 1:",solve(True))
print("Part 2:",solve(False))
