from aoc_utils import *

g = defaultdict(list)
for it in l:
	v = it.split()
	if v[0] == "value":
		g[v[4]+v[5]].append(int(v[1]))
	else:
		g[v[5]+v[6]].append((v[0]+v[1],False))
		g[v[10]+v[11]].append((v[0]+v[1],True))

def getVal(val):
	if isinstance(val,int):
		return val
	return findVal(val[0],val[1])
		
resp1 = None
cache = {}
def findVal(bot,high):
	global resp1
	if (bot,high) in cache:
		return cache[(bot,high)]

	if len(g[bot]) == 1:
		r = getVal(g[bot][0])
	else:
		v1,v2 = getVal(g[bot][0]), getVal(g[bot][1])
		if [v1,v2] in [[61,17],[17,61]]:
			resp1 = bot[3:]
		if high:
			r = max(v1,v2)
		else:
			r = min(v1,v2)
	cache[(bot,high)] = r	
	return r
		
output0 = findVal("output0",False)
output1 = findVal("output1",False)
output2 = findVal("output2",False)
print("Part 1:", resp1)
print("Part 2:", output0*output1*output2)
