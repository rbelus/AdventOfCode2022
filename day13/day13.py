import os
from functools import cmp_to_key

def RecursiveCompare(line1, line2):
	skip = True
	isRight = True
	#print("Comparing", line1, line2)
	if isinstance(line1, list) and isinstance(line2, list):
		for i in range(len(line1)):
			if skip:
				tmpSkip, isRight = RecursiveCompare(line1[i], line2[i] if i < len(line2) else None)
				skip = min(tmpSkip, skip)
			else:
				return skip, isRight
		if skip and len(line1) < len(line2):
			return False, True
	elif isinstance(line1, list) and not isinstance(line2, list):
		if line2 is None:
			skip, isRight = False, False
		else:
			line2 = [line2]
			skip, isRight = RecursiveCompare(line1, line2)
	elif not isinstance(line1, list) and isinstance(line2, list):
		line1 = [line1]
		skip, isRight = RecursiveCompare(line1, line2)
	elif isinstance(line1, int) and isinstance(line2, int):
		skip = line1 == line2
		if not skip:
			isRight = line1 < line2
	else:
		return False, line1 is None
	return skip,isRight
	
# 1st part
input = open(os.path.join(os.path.dirname(__file__), "input"), "r")

tests = []
counter = 0
while True:
	line1 = input.readline()
	if line1 == '':
		break
	line1 = eval(line1)
	line2 = eval(input.readline())
	input.readline()

	tests.append(RecursiveCompare(line1, line2))
	#print(counter, ":", tests[counter][1])
	counter+=1

acc = 0
i = 1
for test in tests:
	if test[1]:
		acc += i
	i += 1

print(acc)

#2nd part
input = open(os.path.join(os.path.dirname(__file__), "input"), "r")
packets = [[[2]], [[6]]]
for line in input.readlines():
	if line == '' or line == '\n':
		continue
	packets.append(eval(line))

def CompareForSort(line1, line2):
	_,isRight = RecursiveCompare(line1, line2)
	if not isRight:
		return -1
	else:
		_,isRight = RecursiveCompare(line2, line1)
		return int(not isRight)

packets = sorted(packets, key=cmp_to_key(CompareForSort), reverse=True)

divider1, divider2 = packets.index([[2]])+1, packets.index([[6]])+1

print(divider1 * divider2)