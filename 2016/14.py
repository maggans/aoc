from aoc_utils import *

def solve(hashings):
	ind = 0
	found = set()
	triplets = defaultdict(set)
	overshoot = 0
	while overshoot < 1000:
		r = hashlib.md5((l[0]+str(ind)).encode()).hexdigest()
		for i in range(hashings - 1):
			r = hashlib.md5(r.encode()).hexdigest()

		tripletfound = False			
		for c,group in groupby(r):
			sz = len(list(group))
			if not tripletfound and sz >= 3:
				triplets[c*3].add(ind)
				tripletfound = True
			if sz >= 5:
				for it in triplets[c*3]:
					if 0 < ind - it <= 1000:
						found.add(it)

		if len(found) > 63:
			overshoot += 1
		ind += 1
	return sorted(found)[63]
	
print("Part 1:", solve(1))
print("Part 2:", solve(2017))
