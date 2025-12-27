from aoc_utils import *

resp1 = resp2 = ""
for it in rot(l,90):
	s = Counter(it)
	resp1 += max(s, key=s.get)
	resp2 += min(s, key=s.get)

print("Part 1:", resp1)
print("Part 2:", resp2)
