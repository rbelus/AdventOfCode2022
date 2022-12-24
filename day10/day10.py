import os
import regex
import numpy as np

class Clock:
	def __init__(self):
		self.cycle = 0
		self.regX = 1
		self.sigStrength = [0 for i in range(6)]
	
	def AddX(self, X):
		self.cycle += 2
		self.CheckStrength()
		self.regX += X
	
	def NoOp(self):
		self.cycle += 1
		self.CheckStrength()

	def CheckStrength(self):
		if self.cycle >= 20 and self.sigStrength[0] == 0:
			self.sigStrength[0] = 20 * self.regX
		elif self.cycle >= 60 and self.sigStrength[1] == 0:
			self.sigStrength[1] = 60 * self.regX
		elif self.cycle >= 100 and self.sigStrength[2] == 0:
			self.sigStrength[2] = 100 * self.regX
		elif self.cycle >= 140 and self.sigStrength[3] == 0:
			self.sigStrength[3] = 140 * self.regX
		elif self.cycle >= 180 and self.sigStrength[4] == 0:
			self.sigStrength[4] = 180 * self.regX
		elif self.cycle >= 220 and self.sigStrength[5] == 0:
			self.sigStrength[5] = 220 * self.regX

class CRT(Clock):
	def __init__(self):
		super().__init__()
		self.screen = np.zeros([6,40], str)
	
	def Draw(self):
		if self.cycle < 241:
			x,y = int((self.cycle-1) % 40), int((self.cycle-1) / 40)
			if abs(x - self.regX) < 2:
				self.screen[y][x] = "#"
			else:
				self.screen[y][x] = " "

	def AddX(self, X):
		self.cycle += 1
		self.Draw()
		self.cycle += 1
		self.Draw()
		self.regX += X
	
	def NoOp(self):
		super().NoOp()
		self.Draw()


# 1st part
input = open(os.path.join(os.path.dirname(__file__), "input"), "r")
addReg = regex.compile(r'^addx (-\d+|\d+)$')
noopReg = regex.compile(r'^noop$')
clock = Clock()

for line in input.readlines():
	m = addReg.match(line)
	if m:
		clock.AddX(int(m.group(1)))
	else:
		clock.NoOp()

print(sum(clock.sigStrength))

#2nd part
input = open(os.path.join(os.path.dirname(__file__), "input"), "r")
crt = CRT()

for line in input.readlines():
	m = addReg.match(line)
	if m:
		crt.AddX(int(m.group(1)))
	else:
		crt.NoOp()

#print(crt.screen)

for row in crt.screen:
	lineString = ""
	for char in row:
		lineString += str(char)
	print(lineString)