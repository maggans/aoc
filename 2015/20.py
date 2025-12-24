from aoc_utils import *

def getPresents(house,valid):
	pres = 0
	for i in range(1,int(house**.5) + 1):
		if house % i == 0:
			if valid(i,house):
				pres += i
			if i**2 != house and valid(house // i,house):
				pres += house // i
	return pres

def solve(p1):
	presents = 0
	house = 0
	while presents < int(l[0]):
		house += 1
		if p1:
			presents = 10 * getPresents(house, lambda a,b : True)
		else:
			presents = 11 * getPresents(house, lambda a,b : a <= b <= 50*a)
	return house
	
print("Part 1:", solve(True))
print("Part 2:", solve(False))
