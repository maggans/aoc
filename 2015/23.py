from aoc_utils import *

def solve(regs):
	i = 0
	while i < len(l):
		v = l[i].split()
		i+=1
		if v[0] == "hlf":
			regs[v[1]] //= 2
		elif v[0] == "tpl":
			regs[v[1]] *= 3
		elif v[0] == "inc":
			regs[v[1]] += 1
		elif v[0] == "jmp":
			i += int(v[1]) - 1
		elif v[0] == "jie" and regs[v[1][:-1]] % 2 == 0:
				i += int(v[2]) - 1
		elif v[0] == "jio" and regs[v[1][:-1]] == 1:
				i += int(v[2]) - 1
	return regs["b"]

print("Part 1:",solve({"a":0,"b":0}))
print("Part 2:",solve({"a":1,"b":0}))
