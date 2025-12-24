from aoc_utils import *

deers = [ints(it) + [0,0] for it in l]
dists = [0] * len(deers)
points = list(dists)
for i in range(2503):
	leaders = []
	best = -1
	for j in range(len(deers)):
		if deers[j][3] < deers[j][1]:
			dists[j] += deers[j][0]
			deers[j][3] += 1
		else:
			deers[j][4] += 1
			if deers[j][4] == deers[j][2]:
				deers[j][3] = deers[j][4] = 0
		if dists[j] == best:
			leaders.append(j)
		elif dists[j] > best:
			best = dists[j]
			leaders = [j]
	for j in leaders:
		points[j] += 1

print("Part 1:", max(dists))
print("Part 2:", max(points))
