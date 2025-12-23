from aoc_utils import *
from z3 import *

resp1 = resp2 = 0		
for line in l:
	light,rest = line.split("]")
	buttons,req = rest.split("{")

	light = [c == "#" for c in light[1:]]
	buttons = [tuple(ints(b)) for b in buttons.split()]
	req = ints(req[:-1])
	
	cache = set()
	q = deque()
	q.append(([0]*len(light),set(buttons)))
	while q:
		cur,remaining_buttons = q.popleft()
		if cur == light:
			resp1 += len(buttons) - len(remaining_buttons)
			break

		if tuple(cur) in cache:
			continue
		cache.add(tuple(cur))
		
		for button in remaining_buttons:
			next = list(cur)
			for ind in button:
				next[ind] = not next[ind]
			q.append((next,remaining_buttons ^ {button}))

	unknowns = [Int("x" + str(i)) for i in range(len(buttons))]
	solver = Optimize()
	for u in unknowns:
		solver.add(u >= 0)
	for i in range(len(req)):
		vars = []
		for j in range(len(buttons)):
			if i in buttons[j]:
				vars.append(Int("x" + str(j)))
		solver.add(sum(vars) == req[i])
	solver.minimize(sum(unknowns))
	solver.check()
	m = solver.model()
	resp2 += sum([m[u].as_long() for u in unknowns])
	
print("Part 1:",resp1)
print("Part 2:",resp2)
