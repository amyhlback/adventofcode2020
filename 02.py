data = list(map(str.split, open("02.txt","r").read().splitlines()))

def part1():
	count = 0
	for i in data:
		j = i[2].count(i[1][0])
		a, b = map(int, i[0].split("-"))
		count += (a <= j and j <= b)
	return count


def part2():
	count = 0
	for i in data:
		a, b = map(lambda x: int(x) -1, i[0].split("-"))
		count += (i[2][a] == i[1][0]) != (i[2][b] == i[1][0])
	return count

print("Day 2")
print("  Part 1:",part1()) #638
print("  Part 2:",part2()) #699