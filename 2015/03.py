from aoc_utils import *

x = y = 0
houses = {(x,y)}
for arrow in l[0]:
	dx,dy = DIRS[arrowToDir(arrow)]
	x+=dx
	y+=dy
	houses.add((x,y))
	
x1 = y1 = x2 = y2 = 0
houses2 = {(x1,y1)}
for i in range(len(l[0])):
	dx,dy = DIRS[arrowToDir(l[0][i])]
	if i % 2 == 0:
		x1+=dx
		y1+=dy
		houses2.add((x1,y1))
	else:
		x2+=dx
		y2+=dy
		houses2.add((x2,y2))
		
print("Part 1:", len(houses))
print("Part 2:", len(houses2))
