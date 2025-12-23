from aoc_utils import *

resp1 = resp2 = 0
corners = [ints(line) for line in l]
areas = []
for (x1,y1),(x2,y2) in combinations(corners,2):
	area = (abs(x1-x2)+1) * (abs(y2-y1)+1)
	areas.append((area,(x1,y1),(x2,y2)))
	resp1 = max(resp1,area)

border = set()
vertical_edges = defaultdict(set)
for i in range(len(corners)):
	x1,y1 = corners[i-1]
	x2,y2 = corners[i]
	if x1 == x2:
		for y in range(min(y1,y2)+1,max(y1,y2)+1):
			border.add((x1,y))
			vertical_edges[y].add(x1)
	else:
		for x in range(min(x1,x2),max(x1,x2)+1):
			border.add((x,y1))

def validpoint(x,y):
	return (x,y) in border or sum([x > edge for edge in vertical_edges[y]]) % 2

def validline(x1,y1,x2,y2):
	if x1 == x2:
		return all(validpoint(x1,y) for y in range(min(y1,y2)+1,max(y1,y2)))
	return all(validpoint(x,y1) for x in range(min(x1,x2)+1,max(x1,x2)))

for area,p1,p2 in sorted(areas,reverse=True):
	p3 = (p1[0],p2[1])
	p4 = (p2[0],p1[1])

	if not validpoint(*p3) or not validpoint(*p4):
		continue

	if all(validline(*start,*end) for start,end in product([p1,p2],[p3,p4])):
		resp2 = area
		break

print("Part 1:",resp1)
print("Part 2:",resp2)
