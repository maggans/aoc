from aoc_utils import *

g = defaultdict(dict)
for it in l:
	v = it[:-1].split()
	g[v[0]][v[-1]] = int(v[3]) * (1 if v[2] == "gain" else -1)

def solve(name,remaining,start):
	remaining.remove(name)
	if len(remaining) == 0:
		remaining.add(name)
		return g[name][start] + g[start][name]
	
	best = -1E10
	for k in remaining:
		best = max(best,g[name][k] + g[k][name] + solve(k,remaining,start))
	remaining.add(name)
	return best
	
print("Part 1:", solve(list(g.keys())[0], set(g.keys()), list(g.keys())[0]))
for k in list(g.keys()):
	g["Myself"][k] = g[k]["Myself"] = 0
print("Part 2:", solve(list(g.keys())[0], set(g.keys()), list(g.keys())[0]))
