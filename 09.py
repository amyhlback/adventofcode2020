with open("inputs/09.txt","r") as f: 
	numbers = list(map(int,f.read().splitlines()))

# yep, quick and dirty: doubly nested loops
def findsum(i, numbers):
	for j in range(1,26):
		for k in range(j,26):
			if numbers[i] == numbers[i-j] + numbers[i-k]:
				return True
	return False

for i in range(25,len(numbers)):
	if not findsum(i, numbers):
		nonsum = numbers[i]
		break

# The worm crawls along the list of numbers eating more if it's to small
# and loosing some tail if it's to large until it reaches the perfect size
tail = 0
head = 1
worm = numbers[tail] + numbers[head]
while worm != nonsum:
	if worm < nonsum:
		head += 1
		worm += numbers[head]
	if nonsum < worm:
		worm -= numbers[tail]
		tail += 1

weakness = min(numbers[tail:head]) + max(numbers[tail:head])

print("Day 9")
print("  Part 1:", nonsum) #756008079
print("  Part 2:", weakness) #93727241
