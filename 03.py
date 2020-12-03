terrain = open("inputs/03.txt","r").read().splitlines()
width = len(terrain[0])
height = len(terrain)

def path(x,y):
	collisions, xpos, ypos = 0,0,0
	while ypos < height:
		collisions += (terrain[ypos][xpos] == "#")
		xpos = (xpos + x) % width
		ypos += y
	return collisions

part2 = path(1,1) * path(3,1) * path(5,1) * path(7,1) * path(1,2)

print("Day 3")
print("  Part 1:", path(3,1)) #228
print("  Part 2:", part2) #6818112000
