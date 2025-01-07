from aoc_utils import *

res = 0

wide = 101
tall = 103
if useExample:
	wide = 11
	tall = 7
	
res2 = 0
robots = []
for line in l:
	a,b = line.split()
	a = a.split("=")
	p1,p2 = a[1].split(",")

	b = b.split("=")
	v1,v2 = b[1].split(",")
	
	robots.append([int(p1),int(p2),int(v1),int(v2)])
	# print(p1,p2,v1,v2)

gr = {}
robotscopy = []
for i in range(9999999999999999):
	gg = {}
	for j in range(len(robots)):
		x = robots[j][0]
		y = robots[j][1]
		x += robots[j][2]
		y += robots[j][3]
		x = x % wide
		y = y % tall
		robots[j][0] = x
		robots[j][1] = y
		gg[(x,y)] = 1
	
	
	# mc = wide//2
	# allFound = True
	# for j in range(40,tall-40):
		# if (mc-1,j) not in gg:
			# allFound = False
			# break
	
	if i == 99:
		robotscopy = copy.deepcopy(robots)
	
	mc = wide // 2
	mr = tall // 2
	wait = False
	for ii in range(wide):
		for jj in range(0,tall-30):
			allFound = True
			for kk in range(29):
				if (ii,jj+kk) not in gg:
					allFound = False
					break
			if allFound:
				wait = True
				break
		if wait:
			break
		
	
	if wait:
		res2 = i+1
		break
		# input("Press enter")
		# for j in range(tall):
			# st = ""
			# for k in range(wide):
				# if (k,j) in gg:
					# st+="#"
				# else:
					# st+="."
			# print(st)
		# print(i,"=============")
		# print(i,"=============")
		# print(i,"=============")
	
#wrong 7891

mc = wide // 2
mr = tall // 2

q1 = 0
q2 = 0
q3 = 0
q4 = 0

for x,y,vx,vy in robotscopy:
	if x < mc and y < mr:
		q1+=1
	if x < mc and y > mr:
		q3+=1
	if x > mc and y < mr:
		q2+=1
	if x > mc and y > mr:
		q4+=1
		
res = q1*q2*q3*q4

print("Part 1:",res)
print("Part 2:",res2)
