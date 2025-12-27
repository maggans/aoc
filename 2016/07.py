from aoc_utils import *

def hasABBA(s):
	for i in range(3,len(s)):
		if s[i] == s[i-3] and s[i-2] == s[i-1] and s[i] != s[i-1]:
			return True
	return False

def getABA(s):
	ret = []
	for i in range(2,len(s)):
		if s[i] == s[i-2] and s[i] != s[i-1]:
			ret.append(s[i-1] + s[i] + s[i-1])
	return ret
	
resp1 = resp2 = 0
for it in l:
	resp1 += hasABBA(it) and not any(hasABBA(r[1:-1]) for r in re.findall("\[\w+\]",it))

	inside = []
	outside = []
	for r in re.findall("\w+|\[\w+\]",it):
		if r[0] == "[":
			outside.append(r[1:-1])
		else:
			inside += getABA(r)
	resp2 += any(ABA in block for block in outside for ABA in inside)
	
print("Part 1:", resp1)
print("Part 2:", resp2)
