from aoc_utils import *

def solve(s,p1):
	r = re.search("\((\d+)x(\d+)\)",s)
	if not r:
		return len(s)
	a,b = int(r.group(1)),int(r.group(2))
	mid = b * a if p1 else b * solve(s[r.end():r.end()+a],p1)
	return len(s[:r.start()]) + mid + solve(s[r.end()+a:],p1)

print("Part 1:", solve(l[0],True))
print("Part 2:", solve(l[0],False))
