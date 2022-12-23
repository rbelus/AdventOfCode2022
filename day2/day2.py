# 1st part
input = open("input", "r")
score = 0
for line in input.readlines():
    him = line[0]
    me = line[2]
    if me == 'X':
        score += 1
        if him == 'A':
            score += 3
        elif him == 'C':
            score += 6
    elif me == 'Y':
        score += 2
        if him == 'B':
            score += 3
        elif him == 'A':
            score += 6
    elif me == 'Z':
        score += 3
        if him == 'C':
            score += 3
        elif him == 'B':
            score += 6
print(score)

# 2nd part
input = open("input", "r")
score = 0
for line in input.readlines():
    him = line[0]
    me = line[2]
    if me == 'X':
        if him == 'A':
            score += 3
        elif him == 'B':
            score += 1
        else:
            score += 2
    elif me == 'Y':
        score += 3
        if him == 'A':
            score += 1
        elif him == 'B':
            score += 2
        else:
            score += 3
    elif me == 'Z':
        score += 6
        if him == 'A':
            score += 2
        elif him == 'B':
            score += 3
        else:
            score += 1
print(score)
