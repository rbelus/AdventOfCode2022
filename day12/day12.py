import os
import sys
import numpy as np
from multiprocessing import Process, Value, Array

INTMAX = 99999999

def MakeTrans():
	chars = "abcdefghijklmnopqrstuvwxyz"
	myDict = {}
	for idx in range(26):
		myDict[chars[idx]] = idx + 1
	myDict['E'] = 26
	myDict['S'] = 1
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
# while distM[yEnd][xEnd] == INTMAX:
# 	for y in range(h):
# 		for x in range(w):
# 			if distM[y][x] != INTMAX:
# 				# UP
# 				if y > 0 and m[y-1][x] <= m[y][x] + 1:
# 					distM[y-1][x] = min(distM[y][x] + 1, distM[y-1][x])
# 				# DOWN
# 				if y < h-1 and m[y+1][x] <= m[y][x] + 1:
# 					distM[y+1][x] = min(distM[y][x] + 1, distM[y+1][x])
# 				# LEFT
# 				if x > 0 and m[y][x-1] <= m[y][x] + 1:
# 					distM[y][x-1] = min(distM[y][x] + 1, distM[y][x-1])
# 				# RIGHT
# 				if x < w-1 and m[y][x+1] <= m[y][x] + 1:
# 					distM[y][x+1] = min(distM[y][x] + 1, distM[y][x+1])

# print(distM[yEnd][xEnd])

#2nd Part

trailStarts = []
trailRanges = []
for y in range(h):
	for x in range(w):
		if m[y][x] == 1:
			trailStarts.append([x, y])

# Distribute workload across threads
trailStartsPerThreadX = [Array('i', int(len(trailStarts) / 12) + 1) for i in range(12)]
trailStartsPerThreadY = [Array('i', int(len(trailStarts) / 12) + 1) for i in range(12)]
startIdx = 0
for start in trailStarts:
	trailStartsPerThreadX[startIdx % 12][int(startIdx / 12)] = start[0]
	trailStartsPerThreadY[startIdx % 12][int(startIdx / 12)] = start[1]
	startIdx += 1

class DjikstraNaiveThread(Process):
	minDist = INTMAX

	def __init__(self, m, trailStartsX, trailStartsY, threadId):
		super().__init__(daemon=True)
		self.m = m
		self.trailStartsX = trailStartsX
		self.trailStartsY = trailStartsY
		self.threadId = threadId
		self.trailRanges = []
		self._target = self.f

	def f(self):
		w, h = len(self.m[0]), len(self.m)
		startIdx, startEnd = 1, len(self.trailStartsX)
		for i in range(startEnd):
			startX, startY = self.trailStartsX[i], self.trailStartsY[i]
			print("Thread : ", self.threadId, " | Computing start", startIdx, "/", startEnd)
			distM = np.full((h,w), INTMAX,int)
			distM[startY][startX] = 0

			# Crazy Djikstra
			tryCounts = 0
			maxDist = 0
			lastDistM = np.full((h,w), INTMAX, int)
			while distM[yEnd][xEnd] == INTMAX:# and tryCounts < w * h:
				lastDistM = np.copy(distM)
				for y in range(h):
					for x in range(w):
						if distM[y][x] != INTMAX:
							# UP
							if y > 0 and self.m[y-1][x] <= self.m[y][x] + 1:
								distM[y-1][x] = min(distM[y][x] + 1, distM[y-1][x])
							# DOWN
							if y < h-1 and self.m[y+1][x] <= self.m[y][x] + 1:
								distM[y+1][x] = min(distM[y][x] + 1, distM[y+1][x])
							# LEFT
							if x > 0 and self.m[y][x-1] <= self.m[y][x] + 1:
								distM[y][x-1] = min(distM[y][x] + 1, distM[y][x-1])
							# RIGHT
							if x < w-1 and self.m[y][x+1] <= self.m[y][x] + 1:
								distM[y][x+1] = min(distM[y][x] + 1, distM[y][x+1])
							maxDist = max(maxDist, distM[y][x])
				if np.array_equal(lastDistM, distM) and tryCounts > 10:
					break
				tryCounts += 1
			self.trailStartsX[i] = distM[yEnd][xEnd]
			self.minDist = min(self.minDist, distM[yEnd][xEnd])
			startIdx += 1

if __name__ == '__main__':
	threads = []
	for thread in range(12):
		threads.append(DjikstraNaiveThread(m, trailStartsPerThreadX[thread], trailStartsPerThreadY[thread], thread))
		threads[thread].start()

	allTrailRanges = []
	for thread in threads:
		thread.join()
		allTrailRanges.append(thread.trailStartsX)

	convertToArray = []
	for trails in allTrailRanges:
		for trail in trails:
			convertToArray.append(trail)
	print(min(convertToArray))