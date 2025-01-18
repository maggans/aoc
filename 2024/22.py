from aoc_utils import *

diffstot = defaultdict(int)
resp1 = 0
for it in l:
	secret = int(it)
	prev = secret
	diffs = []
	diffscache = set()
	for i in range(2000):
		secret = (secret * 64 ^ secret) % 16777216
		secret = (secret // 32 ^ secret) % 16777216
		secret = (secret * 2048 ^ secret) % 16777216
		
		diffs.append(secret % 10 - prev % 10)
		prev = secret
		
		if i > 2:
			seq = "".join([str(x) for x in diffs[i-3:]])
			if seq not in diffscache:
				diffscache.add(seq)
				diffstot[seq]+=secret % 10
	resp1+=secret

print("Part 1:",resp1)
print("Part 2:",max(diffstot.values()))
