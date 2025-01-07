from aoc_utils import *

res = 0

# A - 3 tokens, B - 1 token
g = getGroups(l)

runs=[]
runs2=[]
for it in g:
	a = it[0].split(": ")
	a = a[1].split(", ")
	ax = int(a[0].split("+")[1])
	ay = int(a[1].split("+")[1])

	b = it[1].split(": ")
	b = b[1].split(", ")
	bx = int(b[0].split("+")[1])
	by = int(b[1].split("+")[1])
	
	p = "".join(it[2].split(": "))
	p = p.split(", ")
	px = int(p[0].split("=")[1])
	py = int(p[1].split("=")[1])
	
	runs.append([ax,ay,bx,by,px,py])
	runs2.append([ax,ay,bx,by,px+10000000000000,py+10000000000000])

from z3 import *

for i in range(len(runs)):
	s = Solver()
	x = Int("x")
	y = Int("y")
	s.add(x*runs[i][0] + y*runs[i][2] == runs[i][4])
	s.add(x*runs[i][1] + y*runs[i][3] == runs[i][5])
	if s.check() == sat:
		m = s.model()
		res+=int(str(m[x]))*3+int(str(m[y]))
print("Part 1:",res)

res = 0
for i in range(len(runs2)):
	s = Solver()
	x = Int("x")
	y = Int("y")
	s.add(x*runs2[i][0] + y*runs2[i][2] == runs2[i][4])
	s.add(x*runs2[i][1] + y*runs2[i][3] == runs2[i][5])
	if s.check() == sat:
		m = s.model()
		res+=int(str(m[x]))*3+int(str(m[y]))

print("Part 2:",res)
