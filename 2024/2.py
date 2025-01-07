from aoc_utils import *

res = 0
def isValid(ls):
	v = ls
	first = int(v[0])
	dec = False
	inc = False
	valid = True
	for i in range(1,len(v)):
		a = int(v[i])
		if abs(a-first) <= 0 or abs(a-first) > 3:
			valid = False
			break
		if a > first and dec:
			valid = False
			break
		if a > first:
			inc = True
		if a < first and inc:
			valid = False
			break
		if a < first:
			dec = True
		first = a
	return valid

res1 = 0
for line in l:
	v = line.split()
	val = False
	for i in range(len(v)):
		v2 = copy.deepcopy(v)
		del v2[i]
		if isValid(v2):
			res+=1
			break

	if isValid(line.split()):
		res1+=1
print("Part 1:",res1)
print("Part 2:",res)
