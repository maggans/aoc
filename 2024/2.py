from aoc_utils import *

def isValid(v):
	incr = v[1] > v[0]
	for i in range(1,len(v)):
		if not 1 <= abs(v[i]-v[i-1]) <= 3 or incr != (v[i] > v[i-1]):
			return False
	return True

resp1 = resp2 = 0
for line in l:
	v = ints(line)
	if isValid(v):
		resp1+=1
		continue
	for i in range(len(v)):
		v2 = list(v)
		del v2[i]
		if isValid(v2):
			resp2+=1
			break

print("Part 1:",resp1)
print("Part 2:",resp1+resp2)
