from aoc_utils import *

def solve(nr):
	jolt = 0
	for line in l:
		digs = [int(x) for x in list(line)]
		start = 0
		for i in range(1,nr+1):
			highest = 0
			for j in range(start,len(digs) - nr + i):
				if digs[j] > highest:
					highest = digs[j]
					start = j + 1
			jolt += highest * 10**(nr-i)
	return jolt

print("Part 1:",solve(2))
print("Part 2:",solve(12))
