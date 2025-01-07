from aoc_utils import *

res = 0

l = "".join(l)
ops = re.findall("mul\([\d]+,[\d]+\)", l)

for it in ops:
	factors = ints(it)
	res+=factors[0]*factors[1]

print("Part 1:", res)

ops = re.findall("do\(\)|don't\(\)|mul\([\d]+,[\d]+\)", l)
doMul = True
res = 0
for it in ops:
	if it == "do()":
		doMul = True
	elif it == "don't()":
		doMul = False
	elif doMul:
		factors=ints(it)
		res+=factors[0]*factors[1]
		
print("Part 2:", res)