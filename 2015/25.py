from aoc_utils import *

row,col = ints(l[0])
ind = 1 + (row-1)*row//2 + (col-1)*col//2 + row*(col-1)
code = 20151125
for _ in range(1,ind):
	code = code * 252533 % 33554393

print("Part 1:",code)
print("Part 2:","PUSH DA BUTTON")
