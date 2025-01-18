from aoc_utils import *

g = defaultdict(list)
for line in l:
	a,b = line.split("-")
	g[a].append(b)
	g[b].append(a)	

t_computer_sets = set()
most_computers = []
for comp,neighbors in g.items():
	all_mutual_neighbors = {comp}
	for n1,n2 in combinations(neighbors,2):
		if n1 in g[n2]:
			if any(c.startswith("t") for c in [comp,n1,n2]):
				t_computer_sets.add(frozenset({comp,n1,n2}))
			all_mutual_neighbors |= {n1,n2}

	for n1,n2 in combinations(all_mutual_neighbors,2):
		if n1 not in g[n2] and n1 in all_mutual_neighbors:
			all_mutual_neighbors.remove(n1)

	if len(all_mutual_neighbors) > len(most_computers):
		most_computers = list(all_mutual_neighbors)

print("Part 1:",len(t_computer_sets))
print("Part 2:",",".join(sorted(most_computers)))
