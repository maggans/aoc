from aoc_utils import *

res = 0

x = 0
y = 0
for i in range(len(l)):
	l[i] = list(l[i])
	for j in range(len(l[0])):
		if l[i][j] == "^":
			x = j
			y = i
# print(x,y)
l[y][x] = "."

h = len(l)
w = len(l[0])
def testloop():
	dir = "n"
	vis = {}
	vis[(x,y)] = 1
	v2 = {}
	v2[(x,y,dir)] = 1
	cx = x
	cy = y
	done = False
	while True:
		# print(cx,cy,dir)
		if dir == "n":
			while True:		
				if cy - 1 < 0:
					done = True
					break
				if l[cy-1][cx] == "#":
					dir = "e"
					break
				cy-=1
				vis[(cx,cy)] = 1
				if (cx,cy,dir) in v2:
					return -1
				
				v2[(cx,cy,dir)] = 1
			# print(cx,cy,dir)
			# break
		elif dir == "s":
			while l[cy][cx] != "#":
				if cy + 1 >= h:
					done = True
					break
				if l[cy+1][cx] == "#":
					dir = "w"
					break
					
				cy+=1
				vis[(cx,cy)] = 1
				if (cx,cy,dir) in v2:
					return -1
				
				v2[(cx,cy,dir)] = 1
		
		elif dir == "w":
			while l[cy][cx] != "#":
				if cx - 1 < 0:
					done = True
					break
				if l[cy][cx-1] == "#":
					dir = "n"
					break
				cx-=1
				vis[(cx,cy)] = 1
				if (cx,cy,dir) in v2:
					return -1
				
				v2[(cx,cy,dir)] = 1
		elif dir == "e":
			while l[cy][cx] != "#":
				if cx + 1 >= w:
					done = True
					break
				if l[cy][cx+1] == "#":
					dir = "s"
					break
				cx+=1
				vis[(cx,cy)] = 1
				if (cx,cy,dir) in v2:
					return -1
				
				v2[(cx,cy,dir)] = 1
		if done:
			return len(vis)
	return -1

print("Part 1:",testloop())
	
for i in range(h):
	for j in range(w):
		if i == y and j == x:
			continue
		if l[i][j] == ".":
			l[i][j] = "#"
			if testloop() == -1:
				res+=1
			l[i][j] = "."
print("Part 2:",res)
