from aoc_utils import *

resp1 = resp2 = 0
g = getGroups(l)
ranges = [(int(left),int(right)) for left,right in [x.split("-") for x in g[0]]]
ids = [int(x) for x in g[1]]

for id in ids:
	resp1 += any([left <= id <= right for left,right in ranges])

fresh = []
for left,right in sorted(ranges):
	add = True
	for _,right2 in fresh:
		if left <= right2:
			left = right2 + 1
			if right <= right2:
				add = False
	if add:
		fresh.append((left,right))
		resp2 += right - left + 1

print("Part 1:",resp1)
print("Part 2:",resp2)
