from aoc_utils import *

a,n = [],[]
for line in l:
	disc,sz,_,pos = ints(line)
	a.append(-disc - pos)
	n.append(sz)
	
print("Part 1:", crt(a,n))
print("Part 2:", crt(a + [-len(a) - 1],n + [11]))
