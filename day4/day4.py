import os
import regex

elfAssignReg = regex.compile(r'(\d+)-(\d+),(\d+)-(\d+)')

# 1st part
input = open(os.path.join(os.path.dirname(__file__), "input"), "r")

overlaps = 0
for line in input.readlines():
    m = elfAssignReg.match(line)
    elf1 = (int(m.group(1)), int (m.group(2)))
    elf2 = (int(m.group(3)), int (m.group(4)))
    if (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]) or (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]):
        overlaps += 1

print(overlaps)


# 2nd part
input = open(os.path.join(os.path.dirname(__file__), "input"), "r")

overlaps = 0
for line in input.readlines():
    m = elfAssignReg.match(line)
    elf1 = (int(m.group(1)), int (m.group(2)))
    elf2 = (int(m.group(3)), int (m.group(4)))
    if (min(elf1) <= max(elf2)) and (max(elf1) >= min(elf2)):
        overlaps += 1

print(overlaps)
