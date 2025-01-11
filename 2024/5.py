from aoc_utils import *

g = getGroups(l)
rules = {tuple(ints(x)) for x in g[0]}
pages = [ints(x) for x in g[1]]

res1 = 0
res = 0
for it in pages:
	it2 = sorted(it, key=cmp_to_key(lambda page1, page2: 1 if (page2,page1) in rules else -1))
	if it2 == it:
		res1+=it[len(it)//2]
	else:
		res+=it2[len(it2)//2]
print("Part 1:", res1)
print("Part 2:", res)
