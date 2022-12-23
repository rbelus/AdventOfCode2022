import os
import numpy as np

# 1st part
input = open(os.path.join(os.path.dirname(__file__), "input"), "r")

basicMat = []
for line in input.readlines():
	newRow = []
	for c in line[:-1]:
		newRow.append(int(c))
	basicMat.append(newRow)

npMat = np.array(basicMat, int)
verifMat = np.zeros((len(npMat[0]), len(npMat)), bool)
verifMat[0] = np.clip(verifMat[0], True, True)
verifMat[-1] = np.clip(verifMat[-1], True, True)
verifMat[:,0] = np.clip(verifMat[:,0], True, True)
verifMat[:,-1] = np.clip(verifMat[:,-1], True, True)


w = len(npMat[0])
h = len(npMat)

# Going west
for y in range(1,h-1):
	x = w-1
	currentHeight = 0
	for n in np.flip(npMat[y]):
		if n > currentHeight:
			for westNeighbor in np.flip(npMat[y,0:x]):
				verifMat[y][x] = True
				currentHeight = npMat[y][x]
		x -= 1
# Going east
for y in range(1,h-1):
	x = 0
	currentHeight = 0
	for n in npMat[y]:
		if n > currentHeight:
			for eastNeighbor in npMat[y,x+1:w]:
				verifMat[y][x] = True
				currentHeight = npMat[y][x]
		x += 1
# Going north
for x in range(1,w-1):
	y = h-1
	currentHeight = 0
	for n in np.flip(npMat[:,x]):
		if n > currentHeight:
			for northNeighbor in np.flip(npMat[0:y,x]):
				verifMat[y][x] = True
				currentHeight = npMat[y][x]
		y -= 1
# Going south
for x in range(1,w-1):
	y = 0
	currentHeight = 0
	for n in npMat[:,x]:
		if n > currentHeight:
			for southNeighbor in npMat[y+1:h,x]:
				verifMat[y][x] = True
				currentHeight = npMat[y][x]
		y += 1

print(verifMat.sum())

#2nd part
northMat = np.zeros((len(npMat[0]), len(npMat)), int)
southMat = np.zeros((len(npMat[0]), len(npMat)), int)
eastMat = np.zeros((len(npMat[0]), len(npMat)), int)
westMat = np.zeros((len(npMat[0]), len(npMat)), int)
viewMat = np.zeros((len(npMat[0]), len(npMat)), np.int64)
 

# Going west
for y in range(h):
	x = w-1
	for n in np.flip(npMat[y]):
		currentDist = 0
		for westNeighbor in np.flip(npMat[y,0:x]):
			currentDist += 1
			if westNeighbor >= n:
				break
		westMat[y][x] = currentDist
		x -= 1

# Going east
for y in range(h):
	x = 0
	for n in npMat[y]:
		currentDist = 0
		for eastNeighbor in npMat[y,x+1:w]:
			currentDist += 1
			if eastNeighbor >= n:
				break
		eastMat[y][x] = currentDist
		x += 1

# Going north
for x in range(w):
	y = h-1
	for n in np.flip(npMat[:,x]):
		currentDist = 0
		for northNeighbor in np.flip(npMat[0:y,x]):
			currentDist += 1
			if northNeighbor >= n:
				break
		northMat[y][x] = currentDist
		y -= 1

# Going south
for x in range(w):
	y = 0
	for n in npMat[:,x]:
		currentDist = 0
		for southNeighbor in npMat[y+1:h,x]:
			currentDist += 1
			if southNeighbor >= n:
				break
		southMat[y][x] = currentDist
		y += 1

for y in range(h):
	for x in range(w):
		viewMat[y][x] = np.int64(northMat[y][x])*np.int64(southMat[y][x])*np.int64(eastMat[y][x])*np.int64(westMat[y][x])

print(viewMat.max())