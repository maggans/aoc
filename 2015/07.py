from aoc_utils import *

gates = {}
ops = {"AND":operator.and_,"OR":operator.or_,"LSHIFT":operator.lshift,"RSHIFT":operator.rshift}
for it in l:
	v = it.split()
	if v[1] in ops:
		gates[v[-1]] = [v[0],ops[v[1]],v[2]]
	elif v[0] == "NOT":
		gates[v[-1]] = [v[1],lambda a,_: ~a,"0"]
	else:
		gates[v[-1]] = [v[0],lambda a,_: a,"0"]

cache={}
def calc(gate):
	if gate in cache:
		return cache[gate]
		
	if gate.isdigit():
		return int(gate)

	left,op,right = gates[gate]
	cache[gate] = op(calc(left),calc(right)) & 0xFFFF
	return cache[gate]

print("Part 1:", calc("a"))
cache = {"b":cache["a"]}
print("Part 2:", calc("a"))
