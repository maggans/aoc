from aoc_utils import *

blocked = []
for line in l:
	start,end = line.split("-")
	blocked.append((int(start),int(end)))
blocked = sorted(blocked)

valid = []
if blocked[0][0] > 0:
	valid.append((0,blocked[0][0]-1))
	
for i in range(1,len(blocked)):
	s1,e1 = blocked[i-1]
	s2,e2 = blocked[i]
	if s2-1 <= e1:
		blocked[i] = (s1,max(e1,e2))
	else:
		valid.append((e1+1,s2-1))
	if i == len(blocked) - 1 and max(e1,e2) < 4294967295:
		valid.append((max(e1,e2)+1,4294967295))

print("Part 1:", valid[0][0])
print("Part 2:", sum([end-start+1 for start,end in valid]))
