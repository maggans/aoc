from aoc_utils import *

resp1 = resp2 = 0
d1 = d2 = 50
for line in l:
	val = int(line[1:])
	dx = -1 if line[0] == "L" else 1
	d1 += dx*val
	if not d1 % 100:
		resp1 += 1
	for i in range(val):
		d2 += dx
		if not d2 % 100:
			resp2 += 1	

print("Part 1:",resp1)
print("Part 2:",resp2)
