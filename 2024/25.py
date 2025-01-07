from aoc_utils import *

res = 0

g = getGroups(l)

ks = {}
locks = {}

for i,it in enumerate(g):
	sums = [-1,-1,-1,-1,-1]
	for it2 in it:
		for j in range(len(it2)):
			if it2[j] == "#":
				sums[j] += 1
	if it[0] == "#####":
		locks[i] = sums
	else:
		ks[i] = sums

for k,v in ks.items():
	for kk,vv in locks.items():
		valid = True
		for i in range(len(v)):
			if v[i] + vv[i] > 5:
				valid = False
				break
		if valid:
			res+=1
print("Part 1:",res)
print("Part 2:","PUSH DA BUTTON")



