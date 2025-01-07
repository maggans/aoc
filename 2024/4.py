from aoc_utils import *

res = 0

for line in l:
	for i in range(3,len(line)):
		if line[i-3:i+1] == "XMAS" or line[i-3:i+1] == "SAMX":
			res+=1
			
tl = rot(l,90)
for line in tl:
	line = "".join(line)
	for i in range(3,len(line)):
		if line[i-3:i+1] == "XMAS" or line[i-3:i+1] == "SAMX":
			res+=1

h = len(l)
w = len(l[0])
for y in range(len(l)):
	for x in range(len(l[y])):
		if l[y][x] == "X":
			if y+1<h and x+1<w and l[y+1][x+1] == "M":
				if y+2<h and x+2<w and l[y+2][x+2] == "A":
					if y+3<h and x+3<w and l[y+3][x+3] == "S":
						res+=1
			
			if y-1>=0 and x+1<w and l[y-1][x+1] == "M":
				if y-2>=0 and x+2<w and l[y-2][x+2] == "A":
					if y-3>=0 and x+3<w and l[y-3][x+3] == "S":
						res+=1
					
			if y-1>=0 and x-1>=0 and l[y-1][x-1] == "M":
				if y-2>=0 and x-2>=0 and l[y-2][x-2] == "A":
					if y-3>=0 and x-3>=0 and l[y-3][x-3] == "S":
						res+=1
						
			if y+1<h and x-1>=0 and l[y+1][x-1] == "M":
				if y+2<h and x-2>=0 and l[y+2][x-2] == "A":
					if y+3<h and x-3>=0 and l[y+3][x-3] == "S":
						res+=1

print("Part 1:", res)						
res = 0
for y in range(2,len(l)):
	rows = l[y-2:y+1]
	for x in range(2,len(l[y])):
		rows[0] = l[y-2][x-2:x+1]
		rows[1] = l[y-1][x-2:x+1]
		rows[2] = l[y][x-2:x+1]
		
		if rows[0][0] == "M" and rows[1][1] == "A" and rows[2][2] == "S":
			if rows[0][2] == "M" and rows[2][0] == "S":
				res+=1
			if rows[0][2] == "S" and rows[2][0] == "M":
				res+=1
			
		elif rows[0][0] == "S" and rows[1][1] == "A" and rows[2][2] == "M":
			if rows[0][2] == "M" and rows[2][0] == "S":
				res+=1
			if rows[0][2] == "S" and rows[2][0] == "M":
				res+=1
print("Part 2:", res)
