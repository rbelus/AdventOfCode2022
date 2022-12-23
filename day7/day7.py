import os
import regex
import sys

fileSystemDict = {}

# 1st part
cdReg = regex.compile(r'^\$ cd (.*)$')
lsReg = regex.compile(r'^\$ ls$')
sizeReg = regex.compile(r'^(\d+) (.*)$')
dirReg = regex.compile(r'^dir (.*)$')
stripReg = regex.compile(r'^(.*)\|.*$')
keyReg = regex.compile(r'\w+')
input = open(os.path.join(os.path.dirname(__file__), "input"), "r")

def FindParent(parentDict, subDict):
	for k,v in parentDict.items():
		if isinstance(v, dict):
			if subDict == v:
				print("Found", k, parentDict)
				return parentDict
			else:
				ret = FindParent(v, subDict)
				return ret

def FindParent2(fileDict, parentKey):
	keys = keyReg.findall(parentKey)
	parentDict = fileDict['/']
	for key in keys[:len(keys)-1]:
		parentDict = parentDict[key]
	return parentDict

# construct dict
parentDir = fileSystemDict
parentKey = ''
for line in input.readlines():
	# print('input',line)
	m = cdReg.match(line)
	if m != None:
		dest = m.group(1)
		#dest = dest.strip('/')
		# print('new key', parentKey)
		if dest != '..':
			parentKey += '|' + dest
			parentDir[dest] = {}
			parentDir[dest]['PARENT'] = parentKey
			parentDir = parentDir[dest]
		else:
			#print("cur parent", parentDir, parentKey)
			parentDir = FindParent2(fileSystemDict, parentKey)
			parentKey = stripReg.match(parentKey).group(1)
			#print("changed parent", parentDir, parentKey)
		#continue
	m = sizeReg.match(line)
	if m != None:
		size = int(m.group(1))
		file = m.group(2)
		#if size < 100001:
		parentDir[file] = size
	# print(fileSystemDict, parentDir)

print(fileSystemDict)

# Parse dict and get size of dirs.
def GetDirSize(dirDict, allSmallDirs = None):
	myDirSize = 0
	smallDirs = allSmallDirs
	for k,v in dirDict.items():
		if isinstance(v, dict):
			subDirSize, smallDirs = GetDirSize(v, smallDirs)
			myDirSize += subDirSize
			if subDirSize <= 100000 and allSmallDirs != None:
				smallDirs.append(v)
		elif k != 'PARENT':
			fileSize = int(v)
			myDirSize += fileSize
			print("Adding file ", k, v, dirDict["PARENT"], myDirSize)
	print("DirSize of ", dirDict["PARENT"], myDirSize)
	return myDirSize, smallDirs

allSmallDirs = []
totalSize, allSmallDirs = GetDirSize(fileSystemDict['/'], allSmallDirs)

totalSmallSize = 0
for dir in allSmallDirs:
	totalSmallSize += GetDirSize(dir)[0]

print(totalSmallSize)
