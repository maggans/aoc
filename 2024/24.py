from aoc_utils import *

g = getGroups(l)

gates = {}
regs = {}
z_keys = []

for it in g[0]:
	reg,val = it.split(": ")
	regs[reg] = int(val)

for it in g[1]:
	exp,out = it.split(" -> ")
	left,op,right = exp.split()
	gates[out] = [left,op,right]
	if out[0] == "z":
		z_keys.append(out)
z_keys = sorted(z_keys)

def calc(gate):
	left,op,right = gates[gate]
	if left in regs:
		if op == "XOR":
			return regs[left] ^ regs[right]
		elif op == "AND":
			return regs[left] & regs[right]
		else:
			return regs[left] | regs[right]
	if op == "XOR":
		return calc(left) ^ calc(right)
	elif op == "AND":
		return calc(left) & calc(right)
	else:
		return calc(left) | calc(right)

resp1 = 0
for i,it in enumerate(z_keys):
	z_val = calc(it)
	resp1 += z_val * 2**i
print("Part 1:",resp1)

def isValidCarry(gate,gate_num):
	carry_in = gates[gate]
	if carry_in[1] != "OR":
		# print("wrong OP in carry-in",carry_in)
		return False
	
	prev_gate = format(int(gate_num) - 1).zfill(2)
	prev_gate_x = "x" + prev_gate
	prev_gate_y = "y" + prev_gate
	prev_gate_z = "z" + prev_gate
	
	carry_in_left = set(gates[carry_in[0]])
	carry_in_right = set(gates[carry_in[2]])
	
	prev_z_1,_,prev_z_2 = gates[prev_gate_z]
	
	valid_carry_left = {prev_gate_x,"AND",prev_gate_y}
	valid_carry_right = {prev_z_1,"AND",prev_z_2}
	
	if carry_in_left == valid_carry_left:
		if carry_in_right != valid_carry_right:
			# print("wrong carry right, got",carry_in_right,"but expecting",valid_carry_right)
			return False
	
	elif carry_in_right == valid_carry_left:
		if carry_in_left != valid_carry_right:
			# print("wrong carry left, got",carry_in_left,"but expecting",valid_carry_right)
			return False
	else:
		print("DOUBLE FAILURES OH NOES")
		return False
	return True
	
def isValidGate(gate):
	left,op,right = gates[gate]
	gate_num = gate[1:]
	gate_x_name = "x" + gate_num
	gate_y_name = "y" + gate_num
	to_swap = []
	if op != "XOR":
		# print("wrong OP",left,op,right)
		to_swap.append(gate)
		for k,v in gates.items():
			if set(v) == {gate_x_name,"XOR",gate_y_name}:
				for kk,vv in gates.items():
					if k in vv and "XOR" in vv:
						to_swap.append(kk)
						break
				break		
		return False,to_swap
	
	bit_sum_expr_name = left
	if isValidCarry(left,gate_num):
		bit_sum_expr_name = right
	elif isValidCarry(right,gate_num):
		bit_sum_expr_name = left
	else:
		print("got no valid carry")
		return False,[]

	bit_sum_expr = set(gates[bit_sum_expr_name])
	valid_bit_sum_expr = {gate_x_name,"XOR",gate_y_name}
	
	if bit_sum_expr != valid_bit_sum_expr:
		# print("wrong value expr: got",bit_sum_expr,"but expecting",valid_bit_sum_expr)
		to_swap.append(bit_sum_expr_name)
		for k,v in gates.items():
			if set(v) == valid_bit_sum_expr:
				to_swap.append(k)
				break		
		return False,to_swap
	
	return True,[]

all_swaps = []
for i in range(2,len(z_keys)-1):
	r,swaps = isValidGate(z_keys[i])
	if not r:
		all_swaps += swaps
		gates[swaps[0]],gates[swaps[1]] = gates[swaps[1]],gates[swaps[0]]
print("Part 2:",",".join(sorted(all_swaps)))
