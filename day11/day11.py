import os
import regex
import math

class Monkey:
	monkeys = []
	gcd = 0

	def __init__(self, id, items, worryIncrease, test, trueCase, falseCase):
		self.id = id
		self.items = items
		self.worryIncrease = worryIncrease
		self.test = test
		self.trueCase = trueCase
		self.falseCase = falseCase
		self.inspected = 0

	def Turn(self):
		for item in self.items:
			item = self.Inspect(item)
			self.Throw(item)
		self.items.clear()

	def Inspect(self, item):
		self.inspected += 1
		return int(self.worryIncrease(item) % self.gcd)

	def Throw(self, item):
		if item % self.test == 0:
			self.monkeys[self.trueCase].items.append(item)
		else:
			self.monkeys[self.falseCase].items.append(item)


def CreateLambda(operation, factor):
	match operation:
		case '+':
			if factor == 'old':
				return lambda x: x + x
			else:
				return lambda x: x + int(factor)
		case '*':
			if factor == 'old':
				return lambda x: x * x
			else:
				return lambda x: x * int(factor)

# 1st part
input = open(os.path.join(os.path.dirname(__file__), "input"), "r")
monkeyReg = regex.compile(r'^Monkey (\d+):$')
itemReg = regex.compile(r'^  Starting items: ((\d+|\d+, )+)$')
worryReg = regex.compile(r'^  Operation: new = old (\+|\*) (old|\d+)$')
testReg = regex.compile(r'^  Test: divisible by (\d+)$')
trueReg = regex.compile(r'^    If true: throw to monkey (\d+)$')
falseReg = regex.compile(r'^    If false: throw to monkey (\d+)$')

while True:
	# id
	line = input.readline()
	if not line:
		break
	m = monkeyReg.match(line)
	mId = m.group(1)
	# items
	line = input.readline()
	m = itemReg.match(line)
	itemString = m.group(1).split(',')
	items = []
	for item in itemString:
		item = item.strip(' ')
		items.append(int(item))
	# worry
	line = input.readline()
	m = worryReg.match(line)
	operation = m.group(1)
	factor = m.group(2)
	worryIncrease = CreateLambda(operation, factor)
	# test
	line = input.readline()
	m = testReg.match(line)
	test = int(m.group(1))
	# true
	line = input.readline()
	m = trueReg.match(line)
	true = int(m.group(1))
	# false
	line = input.readline()
	m = falseReg.match(line)
	false = int(m.group(1))
	# empty line
	line = input.readline()

	# Create monkey
	Monkey.monkeys.append(Monkey(mId, items, worryIncrease, test, true, false))

Monkey.gcd = 1
for monkey in Monkey.monkeys:
	Monkey.gcd *= monkey.test

for rounds in range(20):
	for monkey in Monkey.monkeys:
		monkey.Turn()

inspectCounters = []
for monkey in Monkey.monkeys:
	inspectCounters.append(monkey.inspected)

inspectCounters.sort(reverse=True)
print(inspectCounters[0]*inspectCounters[1])

#2nd part
for rounds in range(9980):
	for monkey in Monkey.monkeys:
		monkey.Turn()

inspectCounters = []
for monkey in Monkey.monkeys:
	inspectCounters.append(monkey.inspected)

inspectCounters.sort(reverse=True)
print(inspectCounters[0]*inspectCounters[1])

