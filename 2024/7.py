from aoc_utils import *

def testeq(val,left,match,p2 = False):
	if len(left) == 0:
		return val == match

	if testeq(val * left[0],left[1:],match,p2) or testeq(val + left[0],left[1:],match,p2):
		return True
	if p2 and testeq(int(str(val) + str(left[0])),left[1:],match,p2):
		return True
	return False

res = 0
res2 = 0
for line in l:
	v = ints(line)
	if testeq(v[1],v[2:],v[0]):
		res+=v[0]
	elif testeq(v[1],v[2:],v[0],True):
		res2+=v[0]
print("Part 1:",res)
print("Part 2:",res2+res)
