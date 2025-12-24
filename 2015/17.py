from aoc_utils import *

containers = [int(it) for it in l]
cache = defaultdict(int)

def solve(val,start,end,adds):
	if val == 150:
		cache[adds] += 1
		return 1

	if val > 150:
		return 0
		
	r = 0
	for i in range(start,min(end+1,len(containers))):
		r += solve(val+containers[i],start+1,end+1,adds+1) + solve(val,start+1,end+1,adds)
	return r

print("Part 1:",solve(0,0,0,0))	
print("Part 2:",cache[min(cache.keys())])
