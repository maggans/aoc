from aoc_utils import *

g = getGroups(l)
gates = {}
regs = {}
z_bits = []
ops = {"XOR":operator.xor,"AND":operator.and_,"OR":operator.or_}

for it in g[0]:
	reg,val = it.split(": ")
	regs[reg] = int(val)

for it in g[1]:
	exp,out = it.split(" -> ")
	left,op,right = exp.split()
	gates[out] = [left,ops[op],right]
	if out[0] == "z":
		z_bits.append(out)
z_bits = sorted(z_bits)

def calc(gate):
	left,op,right = gates[gate]
	if left in regs:
		return op(regs[left],regs[right])
	return op(calc(left),calc(right))

print("Part 1:",sum([calc(z) << i for i,z in enumerate(z_bits)]))

def isValidGate(gate):
	left,op,right = gates[gate]
	gate_x = "x" + gate[1:]
	gate_y = "y" + gate[1:]
	if op != ops["XOR"]:
		for (k,v),(kk,vv) in product(gates.items(),repeat=2):
			if set(v) == {gate_x,ops["XOR"],gate_y} and {k,ops["XOR"]}.issubset(set(vv)):
				return False,[gate,kk]	
	
	xor_carry = left
	if gates[left][1] == ops["OR"]:
		xor_carry = right
	valid_xor_carry = {gate_x,ops["XOR"],gate_y}
	
	if set(gates[xor_carry]) != valid_xor_carry:
		for k,v in gates.items():
			if set(v) == valid_xor_carry:
				return False,[xor_carry,k]
	return True,[]

all_swaps = []
for i in range(1,len(z_bits)-1):
	valid,swaps = isValidGate(z_bits[i])
	if not valid:
		all_swaps += swaps
		gates[swaps[0]],gates[swaps[1]] = gates[swaps[1]],gates[swaps[0]]
print("Part 2:",",".join(sorted(all_swaps)))
