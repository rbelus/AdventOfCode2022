import os
# 1st part

def MakeTrans():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    myDict = {}
    for idx in range(0, 52):
        myDict[chars[idx]] = idx + 1
    return myDict

trans = MakeTrans()

# 1st part
input = open(os.path.join(os.path.dirname(__file__), "input"), "r")
priorities = 0
for line in input.readlines():
    end = len(line)
    sack1 = line[0:int(end/2)]
    sack2 = line[int(end/2):end]
    for c in sack1:
        if c in sack2:
            priorities += trans[c]
            break

print(priorities)

# 2nd part
input = open(os.path.join(os.path.dirname(__file__), "input"), "r")
priorities = 0
while True:
    group = [input.readline(), input.readline(), input.readline()]
    if group[0] == '':
        break
    chars = []
    for c in group[0]:
        if c in group[1]:
            chars.append(c)
    for c in chars:
        if c in group[2]:
            priorities += trans[c]
            break

print(priorities)