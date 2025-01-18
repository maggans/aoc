from aoc_utils import *

res = [0,0]
for A,B,P in getGroups(l):
	ax,ay,bx,by,px,py = ints(A+B+P)
	for i,prize in enumerate([0,10000000000000]):
		b = (ax*(py+prize) - ay*(px+prize)) / (ax*by - ay*bx)
		a = ((px+prize) - b*bx) / ax
		if a.is_integer() and b.is_integer():
			res[i] += int(3*a+b)
print("Part 1:",res[0])
print("Part 2:",res[1])
