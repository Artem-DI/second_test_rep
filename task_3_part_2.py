#level 1

'''l = [1, 4, 1, 6, 'hello', 'a', 5, 'hello']
concidence = []

for i in l:
	element = 0
	for x in l:
		if x == i:
			element += 1
	concidence.append(element)      #не мой код, но хотелось бы понять 
                                    #принцип работы, можете объяснить?
dup = set()
index = 0
while index < len(l):
	if concidence[index] > 1:
		dup.add(l[index])
	index +=1

print(dup)'''


#level 2

'''from random import randint

n =5 
m = [[randint(0, 100) for i in range(n)] for j in range(n)]
print(max(max(m)))'''


#level 3

'''d = {'name1': 'id1', 'name2': 'id2', 'name3':'id3'}
b = {}

for key, val in d.items():
	b[val] = key
print()
print(b)'''