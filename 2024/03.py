from aoc_utils import *

l = "".join(l)
ops = re.findall("do\(\)|don't\(\)|mul\([\d]+,[\d]+\)", l)

resp1 = resp2 = 0
doMul = True
for it in ops:
	if it == "do()":
		doMul = True
	elif it == "don't()":
		doMul = False
	else:
		factors=ints(it)
		resp1+=factors[0]*factors[1]
		if doMul:
			resp2+=factors[0]*factors[1]
print("Part 1:", resp1)
print("Part 2:", resp2)
