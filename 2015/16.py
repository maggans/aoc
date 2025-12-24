from aoc_utils import *

tape = {"children":3,"cats": 7,"samoyeds": 2,"pomeranians": 3,"akitas": 0,
				"vizslas": 0,"goldfish": 5,"trees": 3,"cars": 2,"perfumes": 1}

def isValid(item, amount,p2):
	if p2 and item in {"cats","trees"}:
		return item not in tape or tape[item] < amount
	if p2 and item in {"pomeranians","goldfish"}:
		return item not in tape or tape[item] > amount
	return item not in tape or tape[item] == amount
				
for it in l:
	r = re.findall("(\w+):\s(\d+)",it)
	if all(isValid(item,int(amount),False) for item,amount in r):
		print("Part 1:", ints(it)[0])
	if all(isValid(item,int(amount),True) for item,amount in r):
		print("Part 2:", ints(it)[0])
