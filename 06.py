with open("inputs/06.txt","r") as f: 
	data = f.read().splitlines()


# finding all questions answered "yes" to is the combined
# set of all the answers for that group.
def sumyes(data):
	matching = 0
	grouping = set()
	for i in data:
		if i == "":
			matching += len(grouping)
			grouping = set()
		else:
			grouping.update(i)
	return matching + len(grouping)

# questions everyone answered "yes" to is the intersection of all the 
# answers from that group. (using a..z to get complete first answer)
def sumallyes(data):
	matching = 0
	grouping = set('abcdefghijklmnopqrstuvwxyz')
	for i in data:
		if i == "":
			matching += len(grouping)
			grouping = set('abcdefghijklmnopqrstuvwxyz')
		else:
			grouping.intersection_update(i)
	return matching + len(grouping)

print("Day 6")
print("  Part 1:", sumyes(data)) #6170
print("  Part 2:", sumallyes(data)) #2947
