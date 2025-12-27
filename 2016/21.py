from aoc_utils import *

def scramble(password):
	for line in l:
		v = line.split()
		if line.startswith("swap position"):
			x,y = ints(line)
			password[x],password[y] = password[y],password[x]
		elif line.startswith("swap letter"):
			x,y = password.index(v[2]),password.index(v[5])
			password[x],password[y] = password[y],password[x]
		elif line.startswith("rotate based"):
			x = password.index(v[-1])
			password.rotate(1 + x + (x >= 4))
		elif line.startswith("rotate"):
			dir = 1 if v[1] == "right" else -1
			password.rotate(int(v[2])*dir)
		elif line.startswith("reverse"):
			x,y = ints(line)
			p = list(password)
			password = deque(p[:x] + list(reversed(p[x:y+1])) + p[y+1:])
		else:		
			x,y = ints(line)
			p = list(password)
			val = p[x]
			del p[x]
			password = deque(p[:y] + [val] + p[y:])
	return "".join(password)

for it in permutations("abcdefgh"):
	if scramble(deque(it)) == "fbgdceah":
		resp2 = "".join(it)
		break
	
print("Part 1:", scramble(deque("abcdefgh")))
print("Part 2:", resp2)


