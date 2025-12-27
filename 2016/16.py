from aoc_utils import *

def solve(sz):
	a = [c == "1" for c in l[0]]
	while len(a) < sz:
		a += [False] + [not aa for aa in reversed(a)]
	a = a[:sz]
	while len(a) % 2 == 0:
		a = [a[i] == a[i+1] for i in range(0,len(a),2)]
	return "".join(["1" if c else "0" for c in a])
	
print("Part 1:", solve(272))
print("Part 2:", solve(35651584))

