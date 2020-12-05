with open("inputs/05.txt","r") as f: 
	data = f.read().splitlines()

def passtosid(s):
	s = s.translate(str.maketrans("FBLR","0101"))
	row = int(s[:7],2)
	column = int(s[-3:],2)
	return row*8 + column

sids = list(map(passtosid,data))

def findmissing(sids):
	sids = sorted(sids)
	for i in range(len(sids)-1):
		if sids[i+1] == sids[i]+2:
			return sids[i]+1
			
	#No missing sid found, bad input
	return -1

print("Day 5")
print("  Part 1:", max(sids)) #878
print("  Part 2:", findmissing(sids)) # 504