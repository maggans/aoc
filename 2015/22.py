from aoc_utils import *

boss_hp,boss_dmg = ints("".join(l))
spells = [(53,0,0,0,0,4),(73,2,0,0,0,2),(113,0,6,0,0,0),(173,0,0,6,0,0),(229,0,0,0,5,0)]

cache = {}
def solve(hp,mana,my_turn,shield,poison,recharge,boss_hp,p2):
	global boss_dmg
	key = (hp,mana,my_turn,shield,poison,recharge,boss_hp)
	if key in cache:
		return cache[key]

	if my_turn and p2:
		hp-=1
		if hp <= 0:
			return 1e10
			
	if recharge > 0:
		mana += 101
		
	if poison > 0:
		boss_hp -= 3
	if boss_hp <= 0:
		return 0

	best = 1e10
	poison = max(0,poison-1)
	recharge = max(0,recharge-1)
	if my_turn:
		shield = max(0,shield-1)
		charges = [0,0,shield,poison,recharge]
		for i,it in enumerate(spells):
			if mana >= it[0] and charges[i] <= 0:
				r = solve(hp+it[1],mana-it[0],not my_turn,shield+it[2],poison+it[3],recharge+it[4],boss_hp-it[5],p2)
				best = min(best,r + it[0])
	else:
		hp -= max(1,boss_dmg - (shield > 0) * 7)
		if hp > 0:
			best = solve(hp,mana,not my_turn,max(0,shield - 1),poison,recharge,boss_hp,p2)
	
	cache[key] = best
	return best

print("Part 1:",solve(50,500,True,0,0,0,boss_hp,False))
cache = {}
print("Part 2:",solve(50,500,True,0,0,0,boss_hp,True))
