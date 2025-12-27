from aoc_utils import *

def isValidFloor(floor):
	for it in floor:
		if it[1] == "m" and it[0] + "g" not in floor:
			if any(a[1] == "g" for a in floor):
				return False
	return True

cache = {}
vis = set()
def solve(goal,floor,floors):
	if len(floors[3]) == goal:
		return 0

	key = (floor,frozenset(floors[0]),frozenset(floors[1]),frozenset(floors[2]),frozenset(floors[3]))
	if key in cache:
		return cache[key]
	
	if key in vis:
		return 1E20
	vis.add(key)
	
	r = 1E20
	options = [(set(it),[1]) for it in combinations(floors[floor],2)]
	options += [({it},[-1,1]) for it in floors[floor]]
	for group,range in options:
		for i in range:
			if 0 <= floor+i <= 3:
				floors[floor] -= group
				floors[floor+i] |= group
				if isValidFloor(floors[floor]) and isValidFloor(floors[floor+i]):
					r = min(r,1+solve(goal,floor+i,floors))			
				floors[floor+i] -= group
				floors[floor] |= group
	cache[key] = r
	return r

print("Part 1:", solve(10,0,[{"tg","tm","pg","sg"},{"pm","sm"},{"ag","am","rg","rm"},set()]))
cache = {}
vis = set()
sys.setrecursionlimit(2000)
print("Part 2:", solve(14,0,[{"bg","bm","xg","xm","tg","tm","pg","sg"},{"pm","sm"},{"ag","am","rg","rm"},set()]))	
