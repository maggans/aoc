from aoc_utils import *

def solve(rows):
	res = l[0].count(".")
	row = [True] + [tile == "." for tile in l[0]] + [True]
	for _ in range(rows - 1):
		newrow = [True]
		for i in range(1,len(row)-1):
			newrow.append(row[i-1] == row[i+1])
		row = newrow + [True]
		res += sum(row) - 2
	return res

print("Part 1:", solve(40))
print("Part 2:", solve(400000))

