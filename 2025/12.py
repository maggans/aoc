from aoc_utils import *
	
g = getGroups(l)
shapes = [it[1:] for it in g[:-1]]
reqs = g[-1]

sizes = []
allshapes = []
for shape in shapes:
	sizes.append(sum([row.count("#") for row in shape]))
	shapeset = set()
	for angle,axis in product([0,90,180,270],["None","V"]):
		newshape = flip(rot(shape,angle),axis)
		newshapeset = set()
		for x,y in product(range(3),range(3)):
			if newshape[y][x] == "#":
				newshapeset.add((x,y))
		shapeset.add(frozenset(newshapeset))
	allshapes.append(shapeset)
	
sys.setrecursionlimit(3000)
def solve(que,void,placed,match):
	if len(que) == 0:
		return placed == match

	x,y = que.pop()
	nonetested = True
	for i in range(len(allshapes)):
		if placed[i] >= match[i]:
			continue
	
		for shape in allshapes[i]:
			placedshape = set()
			for tx,ty in shape:
				placedshape.add((x+tx,y+ty))
			if len(void & placedshape) != len(placedshape):
				continue
			nonetested = False
			placed[i] += 1
			if solve(que,void ^ placedshape,placed,match):
				return True
			placed[i] -= 1

	if nonetested and solve(que,void,placed,match):
		return True

	que.append((x,y))
	return False
		
res = 0
for req in reqs:
	width,height,*match = ints(req)
	if sum([match[i] * sizes[i] for i in range(len(shapes))]) > width*height:
		continue

	void = set(product(range(width),range(height)))
	que = deque(product(range(width-2),range(height-2)))
	res += solve(que,void,[0]*len(shapes),match)

print("Part 1:",res)
print("Part 2:","PUSH DA BUTTON")
