from aoc_utils import *

res = 0

y = []
eq = []
p2 = False
def testeq(val,left,match, ind):	
	if ind == len(left):
		return val == match

	next = left[ind]
	r1 = val * next
	r2 = val + next
	if testeq(r1,left,match,ind+1) or testeq(r2,left,match,ind+1):
		return True
	if p2 and testeq(int(str(val) + str(next)),left,match,ind+1):
		return True
	return False

for line in l:
	v = line.split(": ")
	y.append(int(v[0]))
	eq.append([int(x) for x in v[1].split()])

y2 = []
eq2 = []
for i in range(len(eq)):
	if testeq(eq[i][0], eq[i][1:], y[i],0):
		res+=y[i]
	else:
		y2.append(y[i])
		eq2.append(eq[i])
print("Part 1:",res)

p2 = True
for i in range(len(eq2)):
	if testeq(eq2[i][0], eq2[i][1:], y2[i],0):
		res+=y2[i]
print("Part 2:",res)
