from aoc_utils import *

disk = []
disk2 = []
free = []
ind = 0
for i in range(len(l[0])):
	val = int(l[0][i])
	if i % 2 == 0:
		disk += ([i//2]*val)
		disk2.append([ind,val])
	else:
		disk += (["."]*val)
		free.append((ind,val))
	ind+=val

res = 0
for i,it in enumerate(disk):
	if it == ".":
		it = disk.pop()
		while disk[-1] == ".":
			disk.pop()
	res += i*it
print("Part 1:", res)

res = 0			
for i in range(len(disk2)-1,-1,-1):
	ind,size = disk2[i]
	for j in range(len(free)):
		f_ind, f_size = free[j]
		if f_ind >= ind:
			break
		if f_size >= size:
			disk2[i][0] = f_ind
			free[j] = (f_ind + size, f_size - size)
			break
	for j in range(size):
		res += (disk2[i][0]+j)*i
print("Part 2:",res)
	