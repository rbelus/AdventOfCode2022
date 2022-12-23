import os

# 1st part
input = open(os.path.join(os.path.dirname(__file__), "input"), "r")

count = 0
found = False
line = input.readline()
while not found:
	sig = line[count:count+4]
	if sig[0] not in sig[1:4] and sig[1] not in sig[2:4] and sig[2] != sig[3]:
		found = True
		break
	count += 1

print(count+4)


# 2nd part
input = open(os.path.join(os.path.dirname(__file__), "input"), "r")

count = 0
found = False
line = input.readline()
while not found:
	sig = line[count:count+14]
	subcount = 0
	subfound = True
	for c in sig:
		subcount += 1
		if c in sig[subcount:14]:
			subfound = False
			break
	if subfound:
		found = True
		break
	count += 1

print(count+14)