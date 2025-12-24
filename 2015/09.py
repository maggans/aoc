from aoc_utils import *

g = defaultdict(list)
for it in l:
	v = it.split()
	g[v[0]].append((v[2],int(v[4])))
	g[v[2]].append((v[0],int(v[4])))

def solve(town,towns_left,p2):
	if len(towns_left) == 0:
		return 0
		
	best = -1E6 if p2 else 1E6
	for next,dist in g[town]:
		if next in towns_left:
			towns_left.remove(next)
			res = dist + solve(next,towns_left,p2)
			best = max(best,res) if p2 else min(best,res)
			towns_left.add(next)
	return best

towns = set(g.keys())
res = [[],[]]
for town in g.keys():
	towns.remove(town)
	res[0].append(solve(town,towns,False))
	res[1].append(solve(town,towns,True))
	towns.add(town)

print("Part 1:",min(res[0]))
print("Part 2:",max(res[1]))
