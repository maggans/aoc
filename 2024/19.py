from aoc_utils import *

res = 0

g = getGroups(l)
towels = g[0][0].split(", ")
patterns = g[1]

cache = {}
def isPossible(pattern,towels):
	if len(pattern) == 0:
		return 1
	
	if pattern in cache:
		return cache[pattern]
	
	matches = 0
	for i in range(1,len(pattern)+1):
		st = pattern[:i]
		if st in towels:
			matches += isPossible(pattern[i:],towels)
	cache[pattern] = matches
	return matches

resp1 = 0
for it in patterns:
	r = isPossible(it,towels)
	res += r
	if r > 0:
		resp1+=1

print("Part 1:",resp1)
print("Part 2:",res)
