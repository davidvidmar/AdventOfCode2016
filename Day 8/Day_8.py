#
# Avent of Code 2016, Day 8
# http://adventofcode.com/2016/day/8
#

import collections

matrixTest = [['.' for i in range(7)] for j in range(3)]
matrix = [['.' for i in range(50)] for j in range(6)]

def rect(x, y, m):
    for row in range(0, y):
        for col in range (0, x):
            m[row][col] = '#'
    return m

def rotCol(x, y, m):
    for i in range(0, y):
        m = rotColDown(x, m)    
    return m

def rotColDown(x, m):
    t = m[len(m)-1][x]
    for row in range(len(m) - 1, 0, -1):
        m[row][x] = m[row-1][x]
    m[0][x] = t
    return m

def rotRow(y, x, m):
    for i in range(0, x):
        m = rotRowRight(y, m)
    return m

def rotRowRight(y, m):
    t = m[y][len(m[y])-1]
    for col in range(len(m[y])-1, 0, -1):
        m[y][col] = m[y][col-1]
    m[y][0] = t
    return m

def printMatrix(matrix):
    for l in matrix:
        for c in l:
            print(c, end="")
        print()        
    print() 

print("Test:")
printMatrix(matrixTest)
matrixTest = rect(3, 2, matrixTest)
printMatrix(matrixTest)
matrixTest = rotCol(1, 1, matrixTest)
printMatrix(matrixTest)
matrixTest = rotRow(0, 4, matrixTest)
printMatrix(matrixTest)
matrixTest = rotCol(1, 1, matrixTest)
printMatrix(matrixTest)
print()

print("Input:")
printMatrix(matrix)
with open("data\input.txt") as f:
    for line in f:
        line = line.strip()
        if line[0:5] == 'rect ':
            param = line[5:].split("x")
            matrix = rect(int(param[0]), int(param[1]), matrix)
            #print("rect ", param[0], param[1])
        elif (line[0:13] == 'rotate row y='):
            param = line[13:].split(" by ")
            matrix = rotRow(int(param[0]), int(param[1]), matrix)
            #print("rot row ", param[0], param[1])
        elif (line[0:16] == 'rotate column x='):
            param = line[16:].split(" by ")
            matrix = rotCol(int(param[0]), int(param[1]), matrix)
            #print("rot col ", param[0], param[1])
        else:
            print("?????????????", line)
print("Final matrix:")
printMatrix(matrix)
cnt = 0
for l in matrix:
    for c in l:
        if c == '#': cnt += 1;
print(cnt)
