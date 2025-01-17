from aoc_utils import *

towels = set(l[0].split(", "))
cache = {}
def isPossible(pattern):
	if len(pattern) == 0:
		return 1
	
	if pattern in cache:
		return cache[pattern]
	
	matches = 0
	for i in range(1,len(pattern)+1):
		if pattern[:i] in towels:
			matches += isPossible(pattern[i:])
	cache[pattern] = matches
	return matches

resp1 = resp2 = 0
for i in range(2,len(l)):
	r = isPossible(l[i])
	resp1 += r > 0
	resp2 += r

print("Part 1:",resp1)
print("Part 2:",resp2)
