from aoc_utils import *

g = defaultdict(list)
for line in l:
	a,b = line.split("-")
	g[a].append(b)
	g[b].append(a)	

ag = {}
ag1 = set()
for k,v in g.items():
	allcons = set()
	allcons.add(k)
	for it in v:
		for it2 in v:
			if it in g[it2]:
				if k[0] == "t" or it[0] == "t" or it2[0] == "t":
					ag1.add(frozenset({k,it,it2}))
				allcons.add(it)
	ag[k] = allcons
			
finalz = {}
for k,v in ag.items():
	alls = True
	v3 = copy.deepcopy(v)
	for it in v:
		for it2 in v:
			if it != it2 and it2 not in g[it] and it in v3:
				v3.remove(it)
	finalz[k] = v3
			
maxl = 0
maxindex = ""
for k,v in finalz.items():
	if len(v) > maxl:
		maxl = len(v)
		maxindex = k

print("Part 1:",len(ag1))
print("Part 2:",",".join(sorted(list(finalz[maxindex]))))
