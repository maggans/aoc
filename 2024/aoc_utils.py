import sys
import copy
from itertools import combinations
from collections import deque, defaultdict, Counter
from string import ascii_lowercase as alc
from functools import cmp_to_key
import hashlib
import heapq
import re
import math
import time
import json

l = []
def readInput(useEx):
	indxx = sys.argv[0].find("aoc\\20") + 9
	indyy = sys.argv[0].find(".py")
	inputday = sys.argv[0][indxx:indyy]
	path = inputday + ".txt"
	if len(sys.argv[0]) < 6:
		path = sys.argv[0][:-3] + ".txt"
	if useEx:
		path = "example.txt"
	global l
	with open(path) as file:
		for line in file:
			if line[-1] == "\n":
				l+=[line[:-1]]
			else:
				l+=[line]

useExample = False
if len(sys.argv) > 1:
	useExample = True
readInput(useExample)

def getGroups(item_list, sep = ""):
	itamz = []
	grouped_itamz = []
	for item in item_list:
		if item == sep:
			grouped_itamz.append(itamz)
			itamz = []
			continue
		itamz.append(item)
	if itamz:
		grouped_itamz.append(itamz)
	return grouped_itamz

def getGroupsN(item_list, n):
	return [item_list[i:i+n] for i in range(0,len(item_list),n)]
	
def printGrid(grid):
	for item in grid:
		print(item)
		
def printGridV(grid):
	for item in grid:
		row = ""
		for item2 in item:
			row+=str(item2)
		print(row)

def lcm(a, b):
  return abs(a*b) // math.gcd(a, b)

def rot(gr,ang):
	grc = copy.deepcopy(gr)
	if ang == 90:
		return list(zip(*grc[::-1]))	
	elif ang == 180:
		r90 = list(zip(*grc[::-1]))
		return list(zip(*r90[::-1]))
	elif ang == 270:
		return list(zip(*grc))[::-1]
	
def flip(gr,dir):
	grc = copy.deepcopy(gr)
	if dir == "H":
		for i in range(len(grc)):
			grc[i] = list(reversed(grc[i]))
		return grc
	else:
		return list(reversed(grc))

def transp(gr):
	return list(zip(*gr))
	
def toBin(val):
	return int(val,2)
	
def binToStr(val,pad=0):
	return format(val, 'b').zfill(pad)

def ints(somearg):
	return [int(x) for x in re.findall('-?\d+',somearg)]

		