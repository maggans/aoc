from aoc_utils import *

l = "".join(l)
ops = re.findall("do\(\)|don't\(\)|mul\([\d]+,[\d]+\)", l)

res = 0
res2 = 0
doMul = True
for it in ops:
	if it == "do()":
		doMul = True
	elif it == "don't()":
		doMul = False
	else:
		factors=ints(it)
		res+=factors[0]*factors[1]
		if doMul:
			res2+=factors[0]*factors[1]
print("Part 1:", res)
print("Part 2:", res2)
