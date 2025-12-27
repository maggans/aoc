from aoc_utils import *

resp1 = resp2 = 0
for i in range(len(l)):
	l[i] = ints(l[i])
	v = sorted(l[i])
	if v[0] + v[1] > v[2]:
		resp1 += 1

for it in getGroupsN(l,3):
	for i in range(3):
		v = sorted([it[0][i], it[1][i], it[2][i]])
		if v[0] + v[1] > v[2]:
			resp2 += 1

print("Part 1:", resp1)
print("Part 2:", resp2)
