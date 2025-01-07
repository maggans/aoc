from aoc_utils import *

h = len(l)
w = len(l[0])
# print(h,w)
res = 0

gard = {}

for i,line in enumerate(l):
	for j in range(w):
		gard[(j,i)] = l[i][j]

vis = {}
groups = defaultdict(list)
for k,v in gard.items():
	group = []
	q = deque()
	if k in vis:
		continue
	q.append(k)
	while q:
		x,y = q.popleft()
		
		if (x,y) in vis:
			continue
		vis[(x,y)] = 1
		group.append((x,y))
		
		dd = [(-1,0),(1,0),(0,-1),(0,1)]
		for dx,dy in dd:
			cx = x+dx
			cy = y+dy
			if (cx,cy) in gard and gard[(cx,cy)] == v:
				q.append((cx,cy))
	groups[v].append(group)
		
p1 = 0
p2 = 0
for k,v in groups.items():
	for it in v:
		res = 0
		area = len(it)
		
		fence = defaultdict(list)
		
		for x,y in it:
			dd = [(-1,0),(1,0),(0,-1),(0,1)]
			per = 4
			for dx,dy in dd:
				cx = x+dx
				cy = y+dy
				if (cx,cy) in it:
					per-=1
				else:
					if cx == x:
						if cy > y:
							fence[(cx,cy,"UV")] = 1
						else:
							fence[(cx,cy,"BV")] = 1
					else:
						if cx > x:
							fence[(cx,cy,"UH")] = 1
						else:
							fence[(cx,cy,"BH")] = 1
			res+=per
			
		fl = 0
		fvis = {}		
		for f,vv in fence.items():		
			if f in fvis:
				continue
			fx,fy,dir = f
			fl+=1
			
			if dir == "UV" or dir == "BV":
				cx = fx+1
				cy = fy
				while (cx,cy,dir) in fence:
					fvis[(cx,cy,dir)] = 1
					cx+=1
				cx = fx-1
				cy = fy
				while (cx,cy,dir) in fence:
					fvis[(cx,cy,dir)] = 1
					cx-=1
			else:
				cx = fx
				cy = fy+1
				while (cx,cy,dir) in fence:
					fvis[(cx,cy,dir)] = 1
					cy+=1
				cx = fx
				cy = fy-1
				while (cx,cy,dir) in fence:
					fvis[(cx,cy,dir)] = 1
					cy-=1
			
		p2+=area*fl
		p1+=area*res

print("Part 1:",p1)
print("Part 2:",p2)
