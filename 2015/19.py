from aoc_utils import *

g = getGroups(l)
m = g[1][0]
replacements = set()
for it in g[0]:
	mol,repl = it.split(" => ")
	for r in re.finditer(mol,m):
		replacements.add(m[:r.start(0)] + repl + m[r.end(0):])
	
print("Part 1:", len(replacements))
print("Part 2:", sum(c.isupper() for c in m) - m.count("Ar") - m.count("Rn") - m.count("Y") * 2 - 1)
