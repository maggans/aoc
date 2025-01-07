from aoc_utils import *

diffstot = defaultdict(int)
resp1 = 0
for it in l:
	secret = int(it)
	diffs = []
	cur = secret % 10	
	diffscache = set()
	for i in range(2000):
		secret = (secret * 64 ^ secret) % 16777216
		secret = (secret // 32 ^ secret) % 16777216
		secret = (secret * 2048 ^ secret) % 16777216

		new = secret % 10
		diffs.append(new - cur)
		cur = new
		
		if i > 2:
			seq = "".join([str(x) for x in diffs[i-3:]])
			if seq not in diffscache:
				diffscache.add(seq)
				diffstot[seq]+=cur
	resp1+=secret

print("Part 1:",resp1)
print("Part 2:",max(diffstot.values()))
