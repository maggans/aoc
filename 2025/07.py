from aoc_utils import *

cache = {}
def findall(x,y):
	if y == len(l) - 1:
		return 1
	
	if (x,y) in cache:
		return cache[(x,y)]
		
	if l[y+1][x] == ".":
		return findall(x,y+1)

	cache[(x,y)] = findall(x-1,y+1) + findall(x+1,y+1)
	return cache[(x,y)]
	
resp2 = findall(*find2d(l, "S"))
print("Part 1:",len(cache))
print("Part 2:",resp2)
