from aoc_utils import *

schematics = [[],[]]
for s in getGroups(l):
	schematics['#' in s[0]].append(sum([1 << i.start() for i in re.finditer('#',"".join(s))]))
print("Part 1:",[lock & key for lock,key in product(*schematics)].count(0))
print("Part 2:", "PUSH DA BUTTON")
