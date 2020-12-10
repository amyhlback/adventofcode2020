with open("inputs/10.txt","r") as f: 
	numbers = sorted(map(int,f.read().splitlines()))

numbers.insert(0,0)
numbers.append(numbers[-1]+3)
size = len(numbers)

ones, threes = 0, 0
for i in range(size-1):
	diff = numbers[i+1] - numbers[i]
	if diff == 1: ones += 1
	elif diff == 3: threes += 1

connections = [0]*size
connections[0] = 1
for i in range(size-1):
	connections[i+1] += connections[i]
	if i+2 < size and numbers[i]+3 >= numbers[i+2]:
		connections[i+2] += connections[i]
	if i+3 < size and numbers[i]+3 >= numbers[i+3]:
		connections[i+3] += connections[i]

print("Day 10")
print("  Part 1:", ones * threes) #2484
print("  Part 2:", connections[-1]) #15790581481472
