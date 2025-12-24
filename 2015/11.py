from aoc_utils import *

def incr(pwd,pos):	
	while True:
		if pwd[pos] == 'z':
			pwd = pwd[:pos] + 'a' + pwd[pos + 1:]
			pos -= 1
			continue
		next_char = chr(ord(pwd[pos]) + 1)
		if next_char in "iol":
			next_char = chr(ord(next_char) + 1) 
		pwd = pwd[:pos] + next_char + pwd[pos + 1:]
		break
	return pwd
	
def isValid(pwd):
	if len(re.findall("[iol]",pwd)) > 0:
		return False

	hasStraight = False
	for i in range(2,len(pwd)):
		if all(ord(pwd[i-j]) - ord(pwd[i-j-1]) == 1 for j in range(2)):
			hasStraight = True
			break
	if not hasStraight:
		return False

	pairs = [i-1 for i in range(1,len(pwd)) if pwd[i] == pwd[i-1]]
	return any(pwd[p1] != pwd[p2] or p2 - p1 > 1 for p1,p2 in combinations(pairs,2))

def findValidPassword(pwd):	
	pwd = incr(pwd,len(pwd) - 1)
	while not isValid(pwd):
		pwd = incr(pwd,len(pwd) - 1)
	return pwd

password = findValidPassword(l[0])
print("Part 1:", password)
print("Part 2:", findValidPassword(password))
