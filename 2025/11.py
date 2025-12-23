from aoc_utils import *

g = {}
for line in l:
	device,neigh = line.split(":")
	g[device] = neigh.split()

cache = defaultdict(int)
def solve(device,dac,fft):
	if device == "out":
		return dac and fft
	
	key = (device,dac,fft)
	if key in cache:
		return cache[key]

	for neigh in g[device]:
		cache[key] += solve(neigh,dac or neigh == "dac",fft or neigh == "fft")
	return cache[key]

print("Part 1:",solve("you",True,True))
print("Part 2:",solve("svr",False,False))
