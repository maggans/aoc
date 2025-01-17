from aoc_utils import *

g1 = {(0,0):"7",(1,0):"8",(2,0):"9",
      (0,1):"4",(1,1):"5",(2,1):"6",
			(0,2):"1",(1,2):"2",(2,2):"3",
			          (1,3):"0",(2,3):"A"}
g2 = {(0,1):"<",(1,1):"v",(2,1):">",(1,0):"^",(2,0):"A"}
grids = [g1,g2]
paths = [defaultdict(set),defaultdict(set)]
for i in range(len(grids)):
	for ((x1,y1),from_key),((x2,y2),to_key) in product(grids[i].items(),repeat=2):
		q = deque([(x1,y1,"")])
		md = abs(x1-x2) + abs(y1-y2)
		while q:
			x,y,path = q.popleft()
			if len(path) > md:
				continue
			if (x,y) == (x2,y2):
				paths[i][(from_key,to_key)].add(path+"A")
				continue
			for dx,dy,dir in [(1,0,">"),(-1,0,"<"),(0,-1,"^"),(0,1,"v")]:
				if (x+dx,y+dy) in grids[i]:
					q.append((x+dx,y+dy,path+dir))

cache = {}
def solve(code,start,level,maxlevel):
	if len(code) == 0:
		return 0
	
	key = (start,code,level)
	if key in cache:
		return cache[key]
	
	minr = 1E20
	for it in paths[level != maxlevel][(start,code[0])]:
		if level == 0:
			len_tmp = len(it) + solve(code[1:],code[0],level,maxlevel)
		else:
			len_tmp = solve(it,"A",level - 1,maxlevel) + solve(code[1:],code[0],level,maxlevel)
		minr = min(len_tmp,minr)		
	cache[key] = minr
	return minr

resp1 = resp2 = 0
for it in l:
	resp1 += solve(it,"A",2,2) * int(it[:-1])
	resp2 += solve(it,"A",25,25) * int(it[:-1])
print("Part 1:",resp1)
print("Part 2:",resp2)	
