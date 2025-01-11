from aoc_utils import *

res = 0
def isValid(v):
	incr = v[1] > v[0]
	for i in range(1,len(v)):
		if not 1 <= abs(v[i]-v[i-1]) <= 3 or incr != (v[i] > v[i-1]):
			return False
	return True

res1 = 0
for line in l:
	v = ints(line)
	if isValid(v):
		res1+=1
		continue
	for i in range(len(v)):
		v2 = copy.deepcopy(v)
		del v2[i]
		if isValid(v2):
			res+=1
			break

print("Part 1:",res1)
print("Part 2:",res1+res)
