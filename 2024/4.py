from aoc_utils import *

def checkRows(rows,p):
	matches=0
	for row in rows:
		for i in range(3,len(row)):
			matches+="".join(row[i-3:i+1]) in p
	return matches

patterns = {"SAMX","XMAS"}
res = checkRows(l,patterns) + checkRows(rot(l,90),patterns)

for y in range(3,len(l)):
	for x in range(3,len(l[y])):
		diag1 = l[y-3][x-3] + l[y-2][x-2] + l[y-1][x-1] + l[y][x]
		diag2 = l[y][x-3] + l[y-1][x-2] + l[y-2][x-1] + l[y-3][x]
		res+= (diag1 in patterns) + (diag2 in patterns)
print("Part 1:", res)

res = 0
patterns = {"SAM","MAS"}
for y in range(2,len(l)):
	for x in range(2,len(l[y])):
		diag1 = l[y-2][x-2] + l[y-1][x-1] + l[y][x]
		diag2 = l[y][x-2] + l[y-1][x-1] + l[y-2][x]
		res+= diag1 in patterns and diag2 in patterns
print("Part 2:", res)
