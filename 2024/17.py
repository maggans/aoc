from aoc_utils import *

ra = ints(l[0])[0]
rb = ints(l[1])[0]
rc = ints(l[2])[0]
prog = ints(l[4])

ip = 0
output = []
while ip < len(prog):
	op = prog[ip]
	next = prog[ip+1]
	nextlit = next
	ip+=2
	if next == 4:
		next = ra
	elif next == 5:
		next = rb
	elif next == 6:
		next = rc		
	
	if op == 0:
		ra //= 2**next
	elif op == 1:
		rb ^= nextlit
	elif op == 2:
		rb = next % 8
	elif op == 3 and ra != 0:
		ip = nextlit
	elif op == 4:
		rb ^= rc
	elif op == 5:
		output.append(str(next % 8))
	elif op == 6:
		rb = ra // 2**next
	elif op == 7:
		rc = ra // 2**next

print("Part 1:",",".join(output))

match = list(reversed(prog))
cands = [(0,8)]
res = []
for j in range(len(match)):
	cc = []
	for s,e in cands:
		for i in range(s,e):
			b = ((((i % 8) ^ 1) ^ (i // 2**((i % 8) ^ 1))) ^ 6) % 8
			if b == match[j]:
				cc.append((i*8,i*8+8))
				if j == len(prog) - 1:
					res.append(i)
	cands = cc
			
print("Part 2:",min(res))
