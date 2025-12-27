from aoc_utils import *

def decrypt(room,id):
	res = ""
	for c in room:
		res += chr(ord("a") + ((ord(c) - ord("a") + id) % (1 + ord("z") - ord("a"))))
	return res

resp1 = resp2 = 0	
for it in l:
	v = it.split("-")
	letters = "".join(v[:-1])
	v = v[-1].split("[")
	id = int(v[0])
	checksum = v[1][:-1]
	
	s = Counter(letters)
	dd = defaultdict(list)
	for a,b in s.items():
		dd[b].append(a)
	dd = sorted([(k,"".join(v)) for k,v in dd.items()])
	most_common = []
	cur = len(dd) - 1
	while len(most_common) < 5:
		for _ in dd[cur][1]:
			most_common.append(dd[cur][1])
		cur-=1
	
	if all(checksum[i] in most_common[i] for i in range(5)):
		resp1 += id
		if "pole" in decrypt(letters,id):
			resp2 = id

print("Part 1:", resp1)
print("Part 2:", resp2)
