from aoc_utils import *

resp1 = resp2 = 0
for it in l:
	vowels = len(re.findall('[aeiou]',it)) >= 3
	consecutive = any(it[i] == it[i-1] for i in range(1,len(it)))
	contains = len(re.findall('ab|cd|pq|xy',it)) == 0
	resp1 += vowels and consecutive and contains
	
	pairs = defaultdict(list)
	hasPair = False
	for i in range(1,len(it)):
		pairs[it[i-1:i+1]].append((i-1,i))
	for v in pairs.values():
		if any(v[i-1][1] != v[i][0] for i in range(1,len(v))):
			hasPair = True
			break
	consecutive = any(it[i] == it[i-2] for i in range(2,len(it)))
	resp2 += hasPair and consecutive

print("Part 1:", resp1)
print("Part 2:", resp2)
