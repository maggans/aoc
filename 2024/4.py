from aoc_utils import *

def checkRows(rows,p):
	matches=0
	for row in rows:
		for i in range(3,len(row)):
			matches+="".join(row[i-3:i+1]) in p
	return matches

patterns = {"SAMX","XMAS"}
resp1 = checkRows(l,patterns) + checkRows(rot(l,90),patterns)

for y in range(3,len(l)):
	for x in range(3,len(l[y])):
		diag1 = "".join([l[y-i][x-i] for i in range(4)])
		diag2 = "".join([l[y-3+i][x-i] for i in range(4)])
		resp1 += (diag1 in patterns) + (diag2 in patterns)
print("Part 1:", resp1)

resp2 = 0
patterns = {"SAM","MAS"}
for y in range(2,len(l)):
	for x in range(2,len(l[y])):
		diag1 = "".join([l[y-i][x-i] for i in range(3)])
		diag2 = "".join([l[y-2+i][x-i] for i in range(3)])
		resp2 += diag1 in patterns and diag2 in patterns
print("Part 2:", resp2)
