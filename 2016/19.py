from aoc_utils import *

sz = int(l[0])
elves = range(sz)
skip_first = False
while sz > 1:
	newelves = []
	for i in range(skip_first,sz,2):
		newelves.append(elves[i])
	skip_first = (sz - skip_first) % 2
	elves = newelves
	sz = len(elves)
resp1 = elves[0] + 1
		
sz = int(l[0])
elves = deque(range(sz))
ind = 0
while sz > 1:
	removed = sz // 2
	elves.rotate(-removed)
	elves.popleft()
	elves.rotate(removed-1)
	ind+=1
	sz -= 1
	
print("Part 1:", resp1)
print("Part 2:", elves[0] + 1)
