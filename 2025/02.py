from aoc_utils import *

resp1 = resp2 = 0
for it in l[0].split(","):
	a,b = it.split("-")
	for i in range(int(a),int(b)+1):
		id = str(i)
		for j in range(2,len(id)+1):
			if id == id[:len(id)//j] * j:
				resp1 += i * (j == 2)
				resp2 += i
				break

print("Part 1:",resp1)
print("Part 2:",resp2)
