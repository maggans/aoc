from aoc_utils import *

a = []
b = []
for line in l:
	c,d = ints(line)
	a.append(c)
	b.append(d)

a = sorted(a)
b = sorted(b)

resp1 = resp2 = 0
for i in range(len(a)):
	resp1 += abs(a[i] - b[i])
	resp2 += b.count(a[i])*a[i]
print("Part 1:",resp1)
print("Part 2:",resp2)
