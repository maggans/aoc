from aoc_utils import *

res = 0

g = getGroups(l)
ra = ints(g[0][0])[0]
rb = ints(g[0][1])[0]
rc = ints(g[0][2])[0]

prog = ints(g[1][0])

ip = 0
ipl = len(prog)
output = []
while ip < ipl:
	op = prog[ip]
	next = prog[ip+1]
	nextlit = next
	if next == 4:
		next = ra
	elif next == 5:
		next = rb
	elif next == 6:
		next = rc		
	
	if 0 <= op <= 3:
		if op == 0:
			ra = ra // (2**next)
		elif op == 1:
			rb = rb ^ nextlit
		elif op == 2:
			rb = next % 8
		elif op == 3:
			if ra != 0:
				ip = nextlit
				continue
	elif op == 4:
		rb = rb ^ rc
	elif op == 5:
		output.append(next % 8)
	elif op == 6:
		rb = ra // (2**next)
	elif op == 7:
		rc = ra // (2**next)
	ip+=2

print("Part 1:",",".join([str(x) for x in output]))

match = list(reversed(prog))
start = 0
end = 8
cands = [(0,8)]
for j in range(len(match)):
	found = False
	cc = []
	for it in cands:
		for i in range(it[0],it[1]):
			b = ((((i % 8) ^ 1) ^ (i // 2**((i % 8) ^ 1))) ^ 6) % 8
			if b == match[j]:
				start = i*8
				end = start+8
				cc.append((start,end))
				if j == len(prog) - 1:
					res = i
					found = True
					break
		if found:
			break
	cands = cc
			
print("Part 2:",res)
