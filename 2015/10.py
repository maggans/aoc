from aoc_utils import *

seq = l[0]
for i in range(50):
	if i == 40:
		print("Part 1:", len(seq))

	res = ""
	for k,v in groupby(seq):
		res += str(len(list(v))) + k
	seq = res
print("Part 2:", len(seq))
