# Day 7 was solved using matrixes and a dash of linear algebra.
# Usually i avoid all imports in AoC, but importing NumPy seems fine since
# the real challenge was solving this using only matrixes, not implementing
# optimized matrix operations.

import numpy as np
with open("inputs/07.txt","r") as f: 
	data = f.read().splitlines()

length = len(data)
bags = {}
bagrules = [0]*length
bagmatrix = np.zeros((length,length))

# First create a dict of all the different bagtypes with index 
# positions and save bagrules to different array
for i in range(length):
	d = data[i][:-1].replace(" bags", "").replace(" bag", "")
	key, rules = d.split(" contain ")
	bags[key] = i
	bagrules[i] = rules.split(", ")

# Set shiny gold to contain 1 of itself (could be seen as adding a matrix
# identifying the element we are interrested in to bagmatrix)
bagmatrix[bags['shiny gold'],bags['shiny gold']] = 1

# Then fill bagmatrix by mapping every bagrule so that each bags rules
# is on a row with contained bags on corresponding columns
for i in range(length):
	for rule in bagrules[i]:
		if rule != "no other":
			amount = rule[0]
			bag = rule[2:]
			bagmatrix[i,bags[bag]] = amount

# Finally multiply bagmatrix with itself until it is stable.
# (the number of multiplications is equal to search depth+1, so
# infinite recursion/looping is a risk if input is bad)
oldmatrix = np.zeros((length,length))
while not (oldmatrix == bagmatrix).all():
	oldmatrix = bagmatrix
	bagmatrix = np.matmul(bagmatrix,bagmatrix)

# A bags row now represent what's inside that bag, thus the sum of
# shiny golds row is the amount of bags in shiny gold, while the
# number of nonzero elements in shiny golds column is the number of bags
# that contain shiny gold.
# (and subtract 1 from both because shiny gold also contains itself)
print("Day 7")
print("  Part 1:", len(list(filter(None, bagmatrix[:,bags['shiny gold']])))-1) #124
print("  Part 2:", sum(bagmatrix[bags['shiny gold'],:])-1) #34862
