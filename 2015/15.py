from aoc_utils import *

ingr = [ints(it) for it in l]
resp1 = resp2 = 0
for it in product(range(101),repeat=len(ingr)-1):
	if sum(it) > 100:
		continue

	last = 100 - sum(it)
	props = [0]*5
	for a,b in zip(list(it)+[last],range(len(ingr))):
		for i in range(5):
			props[i] += a*ingr[b][i]
	props = [max(p,0) for p in props]

	resp1 = max(resp1,reduce(operator.mul, props[:-1]))
	if props[4] == 500:
		resp2 = max(resp2,reduce(operator.mul, props[:-1]))

print("Part 1:", resp1)
print("Part 2:", resp2)
