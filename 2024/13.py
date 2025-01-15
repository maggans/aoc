from aoc_utils import *

res = [0,0]
prize = [0,10000000000000]
for A,B,P in getGroups(l):
	ax,ay,bx,by,px,py = ints(A+B+P)
	for i,dp,in enumerate(prize):
		b = (ax*(py+dp) - ay*(px+dp)) / (ax*by - ay*bx)
		a = ((px+dp) - b*bx) / ax
		if a.is_integer() and b.is_integer():
			res[i] += int(3*a+b)
print("Part 1:",res[0])
print("Part 2:",res[1])
