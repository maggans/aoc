from aoc_utils import *

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
    # | 0 | A |
    # +---+---+
		
    # +---+---+
    # | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+


g = {}
g["9"] = (2,0)
g["8"] = (1,0)
g["7"] = (0,0)
g["6"] = (2,1)
g["5"] = (1,1)
g["4"] = (0,1)
g["3"] = (2,2)
g["2"] = (1,2)
g["1"] = (0,2)
g["0"] = (1,3)
g["A"] = (2,3)

g2 = {}
g2["<"] = (0,1)
g2["v"] = (1,1)
g2[">"] = (2,1)
g2["^"] = (1,0)
g2["A"] = (2,0)

grids = [g,g2]
numpad = "A0123456789"
keypad = "<>^vA"
pads = [numpad,keypad]
paths = [defaultdict(set),defaultdict(set)]
for i in range(len(pads)):
	for c in pads[i]:
		for cc in pads[i]:
			q = deque([(c,"")])
			vis = set()
			md = abs(grids[i][c][0] - grids[i][cc][0]) + abs(grids[i][c][1] - grids[i][cc][1])
			while q:
				next,path = q.popleft()
				if len(path) > md:
					continue
				if next == cc:
					paths[i][(c,cc)].add(path+"A")
					continue
				x = grids[i][next][0]
				y = grids[i][next][1]
				if path in vis:
					continue
				vis.add(path)
				for k,(xd,yd) in grids[i].items():
					if abs(xd-x) + abs(yd-y) == 1:
						if xd < x:
							q.append((k,path+"<"))
						elif xd > x:
							q.append((k,path+">"))
						elif yd < y:
							q.append((k,path+"^"))
						else:
							q.append((k,path+"v"))


def getPaths(start,dig):
	if start in keypad and dig in keypad:
		return paths[1][(start,dig)]
	return paths[0][(start,dig)]
	
cache = {}
def solve(code,startz,level):
	if len(code) == 0:
		return 0
	
	key = (startz,code,level)
	if key in cache:
		return cache[key]
	
	combs = getPaths(startz,code[0])
	minr = 1E20
	
	for it in combs:
		if level == 0:
			len_tmp = len(it) + solve(code[1:],code[0],level)
			minr = min(len_tmp,minr)
		else:
			len_tmp = solve(it,"A",level - 1) + solve(code[1:],code[0],level)
			minr = min(len_tmp,minr)		
	cache[key] = minr
	return minr

res = 0
resp1 = 0
for it in l:
	r = solve(it,"A",25)
	r1 = solve(it,"A",2)
	res+=r*int(it[:-1])
	resp1+=r1*int(it[:-1])
print("Part 1:",resp1)
print("Part 2:",res)	
