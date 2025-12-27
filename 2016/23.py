from aoc_utils import *

def solve(a):
	prog = [line.split() for line in l]
	regs = {"a":a}
	ip = 0
	while ip < len(prog):
		instr,*args = prog[ip]
		is_reg0, is_reg1 = args[0].isalpha(), len(args) > 1 and args[1].isalpha()
		if ip == 4:
			regs["a"] = regs["b"] * regs["d"]
			regs["d"] = 0
			ip += 5
		elif instr == "cpy":
			if is_reg1:
				regs[args[1]] = regs[args[0]] if is_reg0 else int(args[0])
		elif instr == "tgl":
			next = ip + (regs[args[0]] if is_reg0 else int(args[0]))
			if 0 <= next < len(prog):
				if len(prog[next]) == 2:
					if prog[next][0] == "inc":
						prog[next][0] = "dec"
					else:
						prog[next][0] = "inc"
				else:
					if prog[next][0] == "jnz":
						prog[next][0] = "cpy"
					else:
						prog[next][0] = "jnz"
		elif instr == "dec" and is_reg0:
			regs[args[0]] -= 1
		elif instr == "inc" and is_reg0:
			regs[args[0]] += 1
		elif instr == "jnz":
			cond = regs[args[0]] if is_reg0 else int(args[0])
			jump = regs[args[1]] if is_reg1 else int(args[1])
			if cond:
				ip += jump - 1
		ip += 1
	return regs["a"]

print("Part 1:", solve(7))
print("Part 2:", solve(12))
