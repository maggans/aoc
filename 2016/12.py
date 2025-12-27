from aoc_utils import *

def solve(regs):
	ip = 0
	while ip < len(l):
		v = l[ip].split()
		ip += 1
		val = regs[v[1]] if v[1] in regs else int(v[1])
		if v[0] == "cpy":
			regs[v[2]] = val
		elif v[0] == "inc":
			regs[v[1]] += 1
		elif v[0] == "dec":
			regs[v[1]] -= 1
		elif val != 0:
			ip += int(v[2]) - 1
	return regs["a"]
	
print("Part 1:", solve({"a":0,"b":0,"c":0,"d":0}))
print("Part 2:", solve({"a":0,"b":0,"c":1,"d":0}))
