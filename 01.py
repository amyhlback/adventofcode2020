numbers = list(map(int,open("01.txt","r").read().splitlines()))

def part1():
	for i in numbers:
		for j in numbers:
			if i + j == 2020:
				return i*j

def part2():	
	for i in numbers:
		for j in numbers:
			if i + j > 2020 : continue
			for k in numbers:
				if i + j + k == 2020:
					return i*j*k

print("Day 1")
print("  Part 1:", part1()) #969024
print("  Part 2:", part2()) #230057040