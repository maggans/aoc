from aoc_utils import *

resp1 = resp2 = 0
for it in l:
	a,b,c = sorted(ints(it))
	resp1 += 3*a*b + 2*c*(a+b)
	resp2 += 2*(a+b) + a*b*c
print("Part 1:", resp1)
print("Part 2:", resp2)
