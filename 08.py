with open("inputs/08.txt","r") as f: 
	data = f.read().splitlines()

class Computer(object):
	def __init__(self,program):
		self.mem = list(program)
		self.memsize = len(self.mem)
		self.watchdog = [False]*len(self.mem)
		self.accumulator = 0
		self.pointer = 0

	def run(self):
		while True:
			# Exit successfully if eof
			if self.pointer >= self.memsize:
				return 0, self.accumulator

			# Watchdog checking if instruction has already excecuted
			if self.watchdog[self.pointer]:
				return 9, self.accumulator
			self.watchdog[self.pointer] = True

			op, value = self.mem[self.pointer].split()

			self.watchdog[self.pointer] = True

			if op == "acc":
				self.accumulator += int(value)
				self.pointer += 1
				continue

			if op == "nop":
				self.pointer += 1
				continue
			
			if op == "jmp":
				self.pointer += int(value)
				continue

computer = Computer(data)

for i in range(len(data)):
	tmpdata = list(data)
	if tmpdata[i][:3] == "jmp":
		tmpdata[i] = "nop" + tmpdata[i][3:]
	elif tmpdata[i][:3] == "nop":
		tmpdata[i] = "jmp" + tmpdata[i][3:]
	else:
		continue

	tmpcomputer = Computer(tmpdata)
	term, output = tmpcomputer.run()

	if term == 0:
		break

print("Day 8")
print("  Part 1:", computer.run()[1]) #1939
print("  Part 2:", output) #2212
