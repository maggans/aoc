from aoc_utils import *

i = 0
resp1 = ""
resp2 = [""]*8
while True:
	r = hashlib.md5((l[0]+str(i)).encode()).hexdigest()
	if r[:5] == "00000":
		if len(resp1) < 8:
			resp1 += r[5]
		if r[5] < "8" and resp2[int(r[5])] == "":
			resp2[int(r[5])] = r[6]
	if "" not in resp2:
		break
	i+=1

print("Part 1:", resp1)
print("Part 2:", "".join(resp2))
