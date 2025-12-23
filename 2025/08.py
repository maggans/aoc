from aoc_utils import *

resp1 = resp2 = 0
boxes = [ints(line) for line in l]
pairs = []
for (x1,y1,z1),(x2,y2,z2) in combinations(boxes,2):
	d = ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**0.5
	pairs.append((d,(x1,y1,z1),(x2,y2,z2)))
pairs = sorted(pairs)

circs = []
for i,(_,box1,box2) in enumerate(pairs):
	box1_ind = box2_ind = -1
	for j,circ in enumerate(circs):
		if box1 in circ:
			box1_ind = j
		if box2 in circ:
			box2_ind = j

	if box1_ind == -1 and box2_ind == -1:		
		circs.append({box1,box2})
	elif box1_ind == -1:
		circs[box2_ind].add(box1)
	elif box2_ind == -1:
		circs[box1_ind].add(box2)
	elif box2_ind != box1_ind:
		circs[box1_ind] |= circs[box2_ind]
		del circs[box2_ind]

	if i == 1000 - 1:
		sz = sorted([len(circ) for circ in circs])
		resp1 = sz[-1]*sz[-2]*sz[-3]
	
	if len(circs[0]) == len(boxes):
		resp2 = box1[0]*box2[0]
		break
		
print("Part 1:",resp1)
print("Part 2:",resp2)
