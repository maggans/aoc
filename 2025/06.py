from aoc_utils import *

resp1 = resp2 = 0
ops = {"*":operator.mul,"+":operator.add}

g = [line.split() for line in l]
for op,*rest in rot(g,90):
	resp1 += reduce(ops[op],[int(x) for x in rest],op == "*")
	
for it in getGroups(transp(l),(" ",)*len(l)):
	op = it[0][-1]
	vals = [int("".join(it2[:-1])) for it2 in it]
	resp2 += reduce(ops[op],vals,op == "*")
	
print("Part 1:",resp1)
print("Part 2:",resp2)
