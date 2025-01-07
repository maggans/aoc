from aoc_utils import *

h = len(l)
w = len(l[0])

# S facing EAST

sx = 0
sy = 0
ex = 0
ey = 0
for i in range(h):
	l[i] = list(l[i])
for i in range(h):
	for j in range(w):
		if l[i][j] == "S":
			sx = j
			sy = i
			l[i][j] = "."
		if l[i][j] == "E":
			ex = j
			ey = i
			l[i][j] = "."
# print(sx,sy,ex,ey)

q = []
heapq.heappush(q,(0,sx,sy,"e",[]))

vis = {}

paths = set()
bestScore = -1
while q:
	next = heapq.heappop(q)
	score,x,y,dir,path = next
	
	if x == ex and y == ey:
		if bestScore == -1:
			bestScore = score
			paths = paths | set(path)
			paths.add((x,y))
		elif bestScore == score:
			paths = paths | set(path)
		# print(score)
		# paths = paths | set(path)
		# print("path: ",len(set(paths)))
		continue
	
	if (x,y,dir) in vis:
		if vis[(x,y,dir)] != score:
			continue
	vis[(x,y,dir)] = score
	
	if dir == "e":
		if x+1 < w and l[y][x+1] == ".":
			heapq.heappush(q,(score+1,x+1,y,dir,path+[(x,y)]))
		if y-1 >= 0 and l[y-1][x] == ".":
			heapq.heappush(q,(score+1000,x,y,"n",path+[(x,y)]))
		if y+1 < h and l[y+1][x] == ".":
			heapq.heappush(q,(score+1000,x,y,"s",path+[(x,y)]))
		
	elif dir == "w":
		if x-1 >= 0 and l[y][x-1] == ".":
			heapq.heappush(q,(score+1,x-1,y,dir,path+[(x,y)]))
		if y-1 >= 0 and l[y-1][x] == ".":
			heapq.heappush(q,(score+1000,x,y,"n",path+[(x,y)]))
		if y+1 < h and l[y+1][x] == ".":
			heapq.heappush(q,(score+1000,x,y,"s",path+[(x,y)]))
	elif dir == "s":
		if y+1 < h and l[y+1][x] == ".":
			heapq.heappush(q,(score+1,x,y+1,dir,path+[(x,y)]))
		if x-1 >= 0 and l[y][x-1] == ".":
			heapq.heappush(q,(score+1000,x,y,"w",path+[(x,y)]))
		if x+1 < w and l[y][x+1] == ".":
			heapq.heappush(q,(score+1000,x,y,"e",path+[(x,y)]))
	elif dir == "n":
		if y-1 >= 0 and l[y-1][x] == ".":
			heapq.heappush(q,(score+1,x,y-1,dir,path+[(x,y)]))
		if x-1 >= 0 and l[y][x-1] == ".":
			heapq.heappush(q,(score+1000,x,y,"w",path+[(x,y)]))
		if x+1 < w and l[y][x+1] == ".":
			heapq.heappush(q,(score+1000,x,y,"e",path+[(x,y)]))

print("Part 1:", bestScore)
print("Part 2:", len(paths))
