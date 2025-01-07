from aoc_utils import *

res = 0
a = []
b = []
for line in l:
 c,d = line.split()
 a.append(int(c))
 b.append(int(d))

a = sorted(a)
b = sorted(b)

for i in range(len(a)):
	res += abs(a[i] - b[i])
print("Part 1:",res)

res = 0
for i in range(len(a)):
	v = a[i]
	for j in range(len(b)):
		if b[j] == v:
			res+=v
print("Part 2:",res)
