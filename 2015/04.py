from aoc_utils import *

i = 0
resp1 = resp2 = 0
while True:
	i+=1
	r = hashlib.md5((l[0]+str(i)).encode()).hexdigest()
	if r[:5] == "00000" and not resp1:
		resp1 = i
	if r[:6] == "000000" and not resp2:
		resp2 = i
	if resp1 and resp2:
		break
print("Part 1:", resp1)
print("Part 2:", resp2)
