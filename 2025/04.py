from aoc_utils import *

resp1 = resp2 = 0
rolls = set()
for y in range(len(l)):
	for x in range(len(l[0])):
		if l[y][x] == "@":
			rolls.add((x,y))

new_rolls = set()
while len(new_rolls) != len(rolls):
	new_rolls = set(rolls)
	for x,y in new_rolls:
		adj = 0
		for dx,dy in DIRSDIAG:
			if (x+dx,y+dy) in new_rolls:
				adj+=1
		if adj < 4:
			resp2+=1
			rolls.remove((x,y))
	if resp1 == 0:
		resp1 = len(new_rolls) - len(rolls)
	
print("Part 1:",resp1)
print("Part 2:",resp2)
