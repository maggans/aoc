from aoc_utils import *

def solve(numbers,size):
	match = sum(numbers) // size
	i = match // max(numbers) + 1
	best = 1e20
	while best == 1e20:
		for it in combinations(numbers,i):
			if sum(it) == match:
				best = min(best,reduce(operator.mul,it,1))
		i += 1
	return best

print("Part 1:",solve(ints(",".join(l)),3))
print("Part 2:",solve(ints(",".join(l)),4))
