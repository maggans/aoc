from aoc_utils import *

res = 0

g = getGroups(l)
ru = []
for it in g[0]:
	a,b = it.split("|")
	a,b = int(a),int(b)
	ru.append((a,b))

pg = []
for it in g[1]:
	v = it.split(",")
	v = [int(x) for x in v]
	pg.append(v)

def checkRule(page, rule):
	a = 0
	b = 0
	try:
		a = page.index(rule[0])
		b = page.index(rule[1])
	except:
		a = 0
		b = 0
	if a <= b:
		return True
	return False

inc = []
	
for it in pg:
	val = True
	for it2 in ru:
		if not checkRule(it,it2):
			val = False
			break
	if val:
		res+=it[len(it)//2]
	else:
		inc.append(it)

print("Part 1:", res)

res = 0

def fixRule(page, rule):
	a = 0
	b = 0
	try:
		a = page.index(rule[0])
		b = page.index(rule[1])
	except:
		a = 0
		b = 0
		return
	
	if a >= b:
		v = page[a]
		page[a]  = page[b]
		page[b] = v
	else:
		return
		
for it in inc:
	fixed = False
	while not fixed:
		for it2 in ru:
			fixRule(it,it2)
			
		val = True
		for it2 in ru:
			if not checkRule(it,it2):
				val = False
				break
		if val:
			fixed = True
			res+=it[len(it)//2]
print("Part 2:", res)
