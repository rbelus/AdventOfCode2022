import os
import regex

class Knot:
	def __init__(self, parent = None):
		self.parent = parent
		self.curPos = [0,0]

	def Move(self, x, y):
		if not self.parent:
			self.curPos[0] += x
			self.curPos[1] += y
			# print("Parent", x, y, self.curPos)
		else:
			diffPos = [self.curPos[0] - self.parent.curPos[0], self.curPos[1] - self.parent.curPos[1]]
			if abs(diffPos[0]) > 1 or abs(diffPos[1]) > 1:
				self.curPos[0] -= max(-1, min(diffPos[0], 1))
				self.curPos[1] -= max(-1, min(diffPos[1], 1))
			# print("Moving", x, y, self.curPos, diffPos)

class SpecialKnot(Knot):
	def __init__(self, parent):
		super().__init__(parent)
		self.listPreviousPos = []

	def Move(self, x, y):
		super().Move(x, y)
		if '{%s],{%s}'%(self.curPos[0], self.curPos[1]) not in self.listPreviousPos:
			self.listPreviousPos.append('{%s],{%s}'%(self.curPos[0], self.curPos[1]))


# 1st part
input = open(os.path.join(os.path.dirname(__file__), "input"), "r")
moveReg = regex.compile(r'^(\w) (\d+)$')

headKnot = Knot()
follower = SpecialKnot(headKnot)

for line in input.readlines():
	m = moveReg.match(line)
	for i in range(int(m.group(2))):
		match m.group(1):
			case 'U':
				headKnot.Move(0,1)
				follower.Move(0,1)
			case 'D':
				headKnot.Move(0,-1)
				follower.Move(0,-1)
			case 'L':
				headKnot.Move(-1,0)
				follower.Move(-1,0)
			case 'R':
				headKnot.Move(1,0)
				follower.Move(1,0)

print(len(follower.listPreviousPos))

#2nd part
input = open(os.path.join(os.path.dirname(__file__), "input"), "r")
moveReg = regex.compile(r'^(\w) (\d+)$')

headKnot = Knot()
follower = Knot(headKnot)

knots = []
for i in range(9):
	if i > 0:
		knots.append(Knot(knots[i-1]))
	else:
		knots.append(Knot())
knots.append(SpecialKnot(knots[len(knots)-1]))


for line in input.readlines():
	m = moveReg.match(line)
	for i in range(int(m.group(2))):
		match m.group(1):
			case 'U':
				for knot in knots:
					knot.Move(0,1)
				# follower.Move(0,1)
			case 'D':
				for knot in knots:
					knot.Move(0,-1)
				# follower.Move(0,-1)
			case 'L':
				for knot in knots:
					knot.Move(-1,0)
				# follower.Move(-1,0)
			case 'R':
				for knot in knots:
					knot.Move(1,0)
				# follower.Move(1,0)


print(len(knots[len(knots)-1].listPreviousPos))