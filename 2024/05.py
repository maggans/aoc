from aoc_utils import *

g = getGroups(l)
rules = {tuple(ints(x)) for x in g[0]}
pages = [ints(x) for x in g[1]]

res = [0,0]
for p in pages:
	ps = sorted(p, key=cmp_to_key(lambda p1, p2: 1 if (p2,p1) in rules else -1))
	res[ps != p] += ps[len(ps)//2]
print("Part 1:", res[0])
print("Part 2:", res[1])
