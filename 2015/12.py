from aoc_utils import *

def calc(js):
	if isinstance(js, dict):
		if "red" in js.values():
			return 0
		return sum([calc(v) for v in js.values()])
	elif isinstance(js, list):
		return sum([calc(v) for v in js])
	elif isinstance(js, int):
		return js
	return 0

print("Part 1:", sum(ints(l[0])))
print("Part 2:", calc(json.loads(l[0])))
