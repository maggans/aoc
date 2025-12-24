from aoc_utils import *

boss_hp,boss_dmg,boss_ac = ints("".join(l))
weapons = [(8,4),(10,5),(25,6),(40,7),(74,8)]
armors = [(0,0),(13,1),(31,2),(53,3),(75,4),(102,5)]
rings = [(0,0,0),(25,1,0),(50,2,0),(100,3,0),(20,0,1),(40,0,2),(80,0,3)]

def fight(hp,dmg,ac,boss_hp,boss_dmg,boss_ac):
	my_turn = True
	while hp > 0 and boss_hp > 0:
		if my_turn:
			boss_hp -= max(1,dmg - boss_ac)
		else:
			hp -= max(1,boss_dmg - ac)
		my_turn = not my_turn
	return hp > 0
	
def solve(p1):	
	best = 1e10 * p1
	for weapon_cost,weapon_dmg in weapons:
		for armor_cost,armor_ac in armors:
			for ring1,ring2 in list(combinations(rings,2)) + [[(0,0,0),(0,0,0)]]:
				cost = weapon_cost + armor_cost + ring1[0] + ring2[0]
				dmg = weapon_dmg + ring1[1] + ring2[1]
				ac = armor_ac + ring1[2] + ring2[2]
				if p1 == fight(100,dmg,ac,boss_hp,boss_dmg,boss_ac):
					best = min(best,cost) if p1 else max(best,cost)
	return best

print("Part 1:", solve(True))
print("Part 2:", solve(False))
