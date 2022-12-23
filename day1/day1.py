input = open("input", "r")

elves = []

curElfCal = 0
for line in input.readlines():
    if line != '\n':
        curElfCal += int(line)
    else:
        elves.append(curElfCal)
        curElfCal = 0

elves.sort(reverse=True)

print(sum(elves[0:3]))