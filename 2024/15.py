from aoc_utils import *

g = getGroups(l)
gridP1 = [list(x) for x in g[0]]
gridP2 = [[] for _ in gridP1]
sx,sy = find2d(gridP1,"@")
move = "".join(g[1])
for i,it in enumerate(gridP1):
	for j,c in enumerate(it):
		gridP2[i] += [c,c]
		if c == "O":
			gridP2[i] = gridP2[i][:-2] + ["[","]"]
			
def moveVert(grid,x,y,dy,prevy,part2):	
	if grid[y][x] == "]":
		x -= 1
	boxes = [(x,y)]
	toMove = []
	added = set()
	while True:
		toMove += boxes
		boxes_tmp = []
		y+=dy
		for tx,_ in boxes:
			if grid[y][tx] == "#" or (part2 and grid[y][tx+1] == "#"):
				return prevy
			
			for i in [-1,0,1] if part2 else [0]:
				if grid[y][tx+i] in "O[" and (tx+i,y) not in added:
					boxes_tmp.append((tx+i,y))
					added.add((tx+i,y))

		if len(boxes_tmp) == 0:
			for tx,ty in reversed(toMove):
				grid[ty][tx], grid[ty+dy][tx] = grid[ty+dy][tx], grid[ty][tx]
				if part2:
					grid[ty][tx+1], grid[ty+dy][tx+1] = grid[ty+dy][tx+1], grid[ty][tx+1]
			return prevy+dy
		boxes = boxes_tmp

def solve(grid,sx,sy,boxSize,p2):
	x,y = sx,sy
	for arrow in move:
		dx,dy = DIRS[arrowToDir(arrow)]
		nx = x + dx
		ny = y + dy
		
		if grid[ny][nx] == "#":
			continue

		if grid[ny][nx] in "@.":
			x,y = nx,ny
			continue

		if arrow in "<>":
			tx = nx+boxSize*dx
			while grid[y][tx] in "O[]":
				tx += boxSize*dx
			if grid[y][tx] != "#":
				grid[y].insert(nx,grid[y].pop(tx))
				x = nx
		else:
			y = moveVert(grid,nx,ny,dy,y,p2)

	res = 0
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if grid[y][x] in "[O":
				res += 100*y + x
	return res

print("Part 1:",solve(gridP1,sx,sy,1,False))
print("Part 2:",solve(gridP2,sx*2,sy,2,True))
