from aoc_utils import *

w = 101
h = 103
robots = []
grid = [[0]*w for _ in range(h)]
for line in l:
	x,y,vx,vy = ints(line)
	robots.append([x,y,vx,vy])
	grid[y][x]+=1

for i in range(1,w*h):
	for j,[x,y,vx,vy] in enumerate(robots):
		grid[y][x] -= 1
		x = (x + vx) % w
		y = (y + vy) % h
		grid[y][x] +=1
		robots[j] = [x,y,vx,vy]
	
	if i == 100:
		q1 = sum([sum(x[:w//2]) for x in grid[:h//2]])
		q2 = sum([sum(x[w//2+1:]) for x in grid[:h//2]])
		q3 = sum([sum(x[:w//2]) for x in grid[h//2+1:]])
		q4 = sum([sum(x[w//2+1:]) for x in grid[h//2+1:]])
		print("Part 1:", q1*q2*q3*q4)
	
	for ii in range(30,h):
		for jj in range(0,w-30):
			if grid[ii][jj] == 0:
				continue
			if grid[ii][jj:jj+30].count(0) < 5:
				print("Part 2:",i)
				sys.exit()
