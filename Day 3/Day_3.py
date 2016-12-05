#
# Avent of Code 2016, Day 3
# http://adventofcode.com/2016/day/3
#

def check(a, b, c):
    return (a < (b + c)) and (b < (a + c)) and (c < (a + b))        

def part1():

    input = open("data\input.txt", "r") 

    count = 0
    good = 0

    for line in input:
    
        l = line.split()
    
        if len(l) != 3:
            raise ValueError("input not parsed to three values", line, ": ", l)

        a = int(l[0])
        b = int(l[1])
        c = int(l[2])

        if check(a, b, c): 
            good = good + 1

        count = count + 1
     
    print("part 1: ", good, "/", count)

def part2():

    input = open("data\input.txt", "r") 

    count = 0
    good = 0
    i = 0
    t = [0,0,0],[0,0,0],[0,0,0]

    for line in input:
    
        l = line.split()
    
        t[0][i] = int(l[0])
        t[1][i] = int(l[1])
        t[2][i] = int(l[2])

        if (i == 2):            
            for j in range(0, 3):                
                if check(t[j][0], t[j][1], t[j][2]):                                                
                    good = good + 1
                    #print(t[j][0], t[j][1], t[j][2])                    
            i = 0
        else:
            i = i + 1

        count = count + 1
    
    print("part 2: ", good, "/", count)

part1()
part2()