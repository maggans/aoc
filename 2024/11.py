from aoc_utils import *

def solve(iterations):
	d = Counter(ints(l[0]))
	for i in range(iterations):
		dd = defaultdict(int)
		for k,v in d.items():
			its = str(k)
			if k == 0:
				dd[1]+=v
			elif len(its) % 2 == 0:
				left = its[:len(its)//2]
				right = its[len(its)//2:]
				dd[int(left)]+=v
				dd[int(right)]+=v
			else:
				dd[k*2024]+=v
		d = dd
	return sum(d.values())

print("Part 1:",solve(25))
print("Part 2:",solve(75))
