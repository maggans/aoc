from aoc_utils import *

def solve(x,y,passcode):
	if (x,y) == (3,3):
		return passcode, len(passcode)

	doors = hashlib.md5(passcode.encode()).hexdigest()[:4]
	minlen = 1E20
	maxlen = 0
	minpath = None
	for door,(step,dir) in zip(doors,[("U",NORTH),("D",SOUTH),("L",WEST),("R",EAST)]):
		dx,dy = DIRS[dir]
		if door in "bcdef" and 0 <= x + dx <= 3 and 0 <= y + dy <= 3:
			ret1, ret2 = solve(x+dx,y+dy,passcode+step)
			if ret1 and len(ret1) < minlen:
				minlen = len(ret1)
				minpath = ret1
			maxlen = max(maxlen,ret2)
	return minpath, maxlen
	
res = solve(0,0,l[0])
print("Part 1:", res[0][len(l[0]):])
print("Part 2:", res[1] - len(l[0]))

