from aoc_utils import *

res = 0
a = []
b = []
for line in l:
	c,d = ints(line)
	a.append(c)
	b.append(d)

a = sorted(a)
b = sorted(b)

for i in range(len(a)):
	res += abs(a[i] - b[i])
print("Part 1:",res)

res = 0
for v in a:
	for vv in b:
		if vv == v:
			res+=v
print("Part 2:",res)
