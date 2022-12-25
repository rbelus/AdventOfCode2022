import os
import sys
import numpy as np

INTMAX = 99999999

def MakeTrans():
	chars = "abcdefghijklmnopqrstuvwxyz"
	myDict = {}
	for idx in range(26):
		myDict[chars[idx]] = idx + 1
	myDict['E'] = 26
	myDict['S'] = 0
	return myDict

# 1st part
input = open(os.path.join(os.path.dirname(__file__), "input"), "r")
trans = MakeTrans()
array = []
x, y = 0, 0
xStart, yStart = 0, 0
xEnd, yEnd = 0, 0
for line in input.readlines():
	newLine = []
	x = 0
	for char in line[:-1]:
		newLine.append(trans[char])
		if char == 'S':
			xStart, yStart = x, y
		elif char == 'E':
			xEnd, yEnd = x, y
		x += 1
	y += 1

	array.append(newLine)

m = np.array(array)
w, h = len(m[0]), len(m)

distM = np.full((h,w), INTMAX,int)

distM[yStart][xStart] = 0

# Crazy Djikstra
while distM[yEnd][xEnd] == INTMAX:
	for y in range(h):
		for x in range(w):
			if distM[y][x] != INTMAX:
				# UP
				if y > 0 and m[y-1][x] <= m[y][x] + 1:
					distM[y-1][x] = min(distM[y][x] + 1, distM[y-1][x])
				# DOWN
				if y < h-1 and m[y+1][x] <= m[y][x] + 1:
					distM[y+1][x] = min(distM[y][x] + 1, distM[y+1][x])
				# LEFT
				if x > 0 and m[y][x-1] <= m[y][x] + 1:
					distM[y][x-1] = min(distM[y][x] + 1, distM[y][x-1])
				# RIGHT
				if x < w-1 and m[y][x+1] <= m[y][x] + 1:
					distM[y][x+1] = min(distM[y][x] + 1, distM[y][x+1])

print(distM[yEnd][xEnd])