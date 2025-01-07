from aoc_utils import *

g = getGroups(l)

grid2 = []
grid3 = g[0]
gridP1 = {}
sxp1 = 0
syp1 = 0
for i,it in enumerate(grid3):
	ng = ""
	for j,c in enumerate(it):
		gridP1[(j,i)] = c
		if c == "#":
			ng+="##"
		elif c == "O":
			ng+="[]"
		elif c == ".":
			ng+=".."
		else:
			sxp1 = j
			syp1 = i
			gridP1[(j,i)] = "."
			ng+="@."
	grid2.append(ng)

move = ""

def printgg(gr):
	for i in range(20):
		st = ""
		for j in range(20):
			if (j,i) in gr:
				st += gr[(j,i)]
		if st:
			print(st)

sx = 0
sy = 0
grid = {}
for i,c in enumerate(grid2):
	for j,cc in enumerate(c):
		grid[(j,i)] = cc
		if cc == "@":
			sx = j
			sy = i

for it in g[1]:
	move += it

grid[(sx,sy)] = "."

def moveVert(gg,x,y,ddy):
	if (x,y) not in gg:
		return -1
	
	if gg[(x,y)] == ".":
		return 0
	
	x1 = x
	x2 = x
	if gg[(x,y)] == "[":
		x1 = x
		x2 = x+1
	if gg[(x,y)] == "]":
		x1 = x-1
		x2 = x
	boxes = [(x1,y)]
	toMove = []
	while True:
		bb = []
		y+=ddy
		toMove += boxes
		for it in boxes:
			xx = it[0]
			xx2 = xx+1
			
			if (xx,y) not in gg or (xx+1,y) not in gg:
				return -1
			if gg[(xx,y)] == "#" or gg[(xx+1,y)] == "#":
				return -1
			
			if gg[(xx,y)] == "[":
				bb.append((xx,y))
			elif gg[(xx,y)] == "]":
				bb.append((xx-1,y))
			if gg[(xx+1,y)] == "[":
				bb.append((xx+1,y))
		if len(bb) == 0:
			vis = {}
			for it in reversed(toMove):
				mx = it[0]
				my = it[1]
				if (mx,my) in vis:
					continue
				vis[(mx,my)] = 1
				if gg[(mx,my)] == "[":
					gg[(mx,my+ddy)] = "["
					gg[(mx,my)] = "."
					gg[(mx+1,my+ddy)] = "]"
					gg[(mx+1,my)] = "."
			return 0
		boxes = bb

def moveHori(gg,x,y,ddx):
	updates = []
	tx = x
	ty = y
	while (tx,ty) in grid and (grid[(tx,ty)] == "[" or grid[(tx,ty)] == "]"):
		updates.append((tx,ty))
		tx += ddx + ddx
	if (tx,ty) in grid and grid[(tx,ty)] == ".":
		# cx = nx
		# cy = ny
		for it in reversed(updates):
			if grid[(it[0],it[1])] == "[":
				grid[(it[0]+ddx,it[1])] = "["
				grid[(it[0]+ddx+ddx,it[1])] = "]"
			elif grid[(it[0],it[1])] == "]":
				grid[(it[0]+ddx,it[1])] = "]"
				grid[(it[0]+ddx+ddx,it[1])] = "["
			else:
				print("err")
		grid[(x,y)] = "."
		return 0
	return -1

def solve(p1 = False):
	global grid
	grid_c = copy.deepcopy(grid)
	cx = sx
	cy = sy
	if p1:
		grid = gridP1
		cx = sxp1
		cy = syp1
	for dir in move:
		# print(cx,cy,dir)
		dx = 0
		dy = 0
		if dir == "<":
			dx = -1
		elif dir == ">":
			dx = 1
		elif dir == "v":
			dy = 1
		else:
			dy = -1
			
		nx = cx + dx
		ny = cy + dy
		if (nx,ny) in grid:
			if grid[(nx,ny)] == "#":
				continue
			if grid[(nx,ny)] == ".":
				cx = nx
				cy = ny
			else:
				if not p1:
					if dir == "<" or dir == ">":
						if moveHori(grid,nx,ny,dx) == 0:
							cx = nx			
					else:
						if moveVert(grid,nx,ny,dy) == 0:
							cy = ny
				else:
					updates = []
					tx = nx
					ty = ny
					while (tx,ty) in grid and grid[(tx,ty)] == "O":
						updates.append((tx,ty))
						tx += dx
						ty += dy
					if (tx,ty) in grid and grid[(tx,ty)] == ".":
						cx = nx
						cy = ny
						grid[(nx,ny)] = "."
						grid[(tx,ty)] = "O"
						# for ttx,tty in updates:
							# grid[(ttx,tty)] = "O"
	
		# printgg(grid)
		# print()
	res2 = 0
	for k,v in grid.items():
		if v == "[" or p1 and v == "O":
			res2+=((100*k[1]) + k[0])
	grid = grid_c
	return res2

print("Part 1:",solve(True))
print("Part 2:",solve(False))
