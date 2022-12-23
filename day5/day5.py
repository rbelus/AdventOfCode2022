import os
import regex

boxReg = regex.compile(r'(?>(?>\[(\w)\]| ( ) )(?> |\n))')
nbReg = regex.compile(r'\d+')

# 1st part
input = open(os.path.join(os.path.dirname(__file__), "input"), "r")

boxes = []
coords = []
while True:
	line = input.readline()
	mList = boxReg.findall(line)
	if len(mList) == 0:
		for m in nbReg.findall(line):
			coords.append(int(m[0]))
		break
	for m in mList:
		boxes.append(m[0])

stacks = [[] for i in range(0, max(coords))]
t = 0
while t < len(boxes):
	for stackIdx in range(0, max(coords)):
		currentBox = boxes[t]
		t += 1
		if currentBox != '':
			stacks[stackIdx].append(currentBox)

for line in input.readlines():
	mList = nbReg.findall(line)
	if len(mList) > 0: 
		nbOp = int(mList[0])
		source = int(mList[1])-1
		target = int(mList[2])-1
		for op in range(0, nbOp):
			if len(stacks[source]) > 0:
				stacks[target].insert(0, stacks[source].pop(0))

ret = ''
for stack in stacks:
	ret += stack[0]

print(ret)

# 2nd part
input = open(os.path.join(os.path.dirname(__file__), "input"), "r")

boxes = []
coords = []
while True:
	line = input.readline()
	mList = boxReg.findall(line)
	if len(mList) == 0:
		for m in nbReg.findall(line):
			coords.append(int(m[0]))
		break
	for m in mList:
		boxes.append(m[0])

stacks = [[] for i in range(0, max(coords))]
t = 0
while t < len(boxes):
	for stackIdx in range(0, max(coords)):
		currentBox = boxes[t]
		t += 1
		if currentBox != '':
			stacks[stackIdx].append(currentBox)

for line in input.readlines():
	mList = nbReg.findall(line)
	if len(mList) > 0: 
		nbCrates = int(mList[0])
		source = int(mList[1])-1
		target = int(mList[2])-1
		# me forgot how to seq list, me dumb dumb 
		# me cant make slicing step work
		stackmove = stacks[source][0:nbCrates]
		stackmove.reverse()
		for box in stackmove:	
			stacks[target].insert(0, box)
		for i in range(0,nbCrates):
			if len(stacks[source]) > 0:
				stacks[source].pop(0)

ret = ''
for stack in stacks:
	ret += stack[0]

print(ret)