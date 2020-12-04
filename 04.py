with open("inputs/04.txt","r") as f: 
	data = f.read().splitlines()

passports = [{}]
for p in data:
	if p == "":
		passports.append({})
	else:
		for d in p.split():
			passports[-1][d[:3]] = d[4:]

def easyvalidate(p):
	for i in ['byr','iyr','eyr','hgt','hcl','ecl','pid']:
		if i not in p:
			return False
	return True

def strictvalidate(p):
	#Catches both malformed values and missing keys
	try:
		if int(p['byr']) < 1920 or 2002 < int(p['byr']): return False

		if int(p['iyr']) < 2010 or 2020 < int(p['iyr']): return False

		if int(p['eyr']) < 2020 or 2030 < int(p['eyr']): return False

		if p['hgt'].endswith("cm"):
			if int(p['hgt'][:-2]) < 150 or 193 < int(p['hgt'][:-2]): return False
		elif p['hgt'].endswith("in"):
			if int(p['hgt'][:-2]) < 59 or 76 < int(p['hgt'][:-2]): return False
		else:
			return False

		if not(p['hcl'].startswith("#") and p['hcl'][1:].isalnum()): return False

		if p['ecl'] not in ["amb","blu","brn","gry","grn","hzl","oth"]: return False

		if len(p['pid']) != 9 or not p['pid'].isdecimal(): return False

	except:
		return False

	return True

print("Day 4")
print("  Part 1:", sum(map(easyvalidate, passports))) #256
print("  Part 2:", sum(map(strictvalidate, passports))) #198
