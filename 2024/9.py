from aoc_utils import *

h = len(l)
w = len(l[0])
# print(h,w)
res = 0

free = False
id = 0
ff = {}
disk = defaultdict(int)

ll = []

for i in range(w):
	if free:
		disk[id]+=int(l[0][i])
		id+=1
		for j in range(int(l[0][i])):
			ll.append(-1)
	else:
		for j in range(int(l[0][i])):
			ll.append(id//2)
		disk[id]+=int(l[0][i])
		id+=1
	
	free = not free
			
def fits(sz,sind):
	startind = 0
	while True:
		try:
			ind = ll.index(-1,startind+1)
			if ind > sind:
				return -1
			
			endind = ind
			for j in range(ind,len(ll)):
				if ll[endind+1] == -1:
					endind+=1
				else:
					break
					
			if (endind - ind +1 ) >= sz:
				return ind
			startind = endind
		except:
			return -1

	return -1

ids_to_check = []
for k,v in disk.items():
	if k % 2 == 0 and k > 0:
		ids_to_check.append(k//2)
		
llp1 = copy.deepcopy(ll)

while ids_to_check:
	id = ids_to_check.pop()
	# print(id)
	idsz = disk[id*2]
	ss = ll.index(id)
	sse = ss+idsz
	fid = fits(idsz,ss)	
	if fid == -1:
		continue
	for i in range(idsz):
		ll[fid+i] = id
		ll[sse-i-1] = -1

while True:
	try:
		last = llp1[-1]
		if last == -1:
			last = llp1.pop()
			continue
		ind = llp1.index(-1)
		llp1[ind] = llp1.pop()
	except:
		break

resp1=0

for i in range(len(llp1)):
	resp1+= i*llp1[i]

for i in range(len(ll)):
	if ll[i] != -1:
		res+= i*ll[i]

print("Part 1:",resp1)
print("Part 2:",res)
	