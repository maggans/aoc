from aoc_utils import *

def solve(a):
	regs = {"a":a}
	output = [1]
	ip = 0
	while ip < len(l):
		v = l[ip].split()
		ip += 1
		val = regs[v[1]] if v[1] in regs else int(v[1])
		if v[0] == "out":
			if val == output[-1]:
				return False
			if len(output) > 100:
				return True
			output.append(val)
		elif v[0] == "cpy":
			regs[v[2]] = val
		elif v[0] == "inc":
			regs[v[1]] += 1
		elif v[0] == "dec":
			regs[v[1]] -= 1
		elif val != 0:
			ip += int(v[2]) - 1
	return regs["a"]
	
resp1 = 0
while not solve(resp1):
	resp1 += 1
	
print("Part 1:", resp1)
print("Part 2:", "PUSH DA BUTTON")
