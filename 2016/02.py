from aoc_utils import *

g1 = {(i%3,i//3):str(i+1) for i in range(9)}
g2 = {(2,0):"1",(1,1):"2",(2,1):"3",(3,1):"4",(0,2):"5",(1,2):"6",(2,2):"7",(3,2):"8",
      (4,2):"9",(1,3):"A",(2,3):"B",(3,3):"C",(2,4):"D"}
dd = {"U":(0,-1),"D":(0,1),"L":(-1,0),"R":(1,0)}
grids = [g1,g2]
res = ["",""]
pos = [[1,1],[0,2]]
for it in l:
	for i in range(2):
		for c in it:
			if (pos[i][0]+dd[c][0],pos[i][1]+dd[c][1]) in grids[i]:
				pos[i][0] += dd[c][0]
				pos[i][1] += dd[c][1]
		res[i] += grids[i][tuple(pos[i])]

print("Part 1:", res[0])
print("Part 2:", res[1])
