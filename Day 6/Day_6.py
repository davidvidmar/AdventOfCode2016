#
# Avent of Code 2016, Day 6
# http://adventofcode.com/2016/day/6
#

import collections

def errorCorrect(file):
    with open(file) as f:
        l = [list(x) for x in f]

    message = [];
    for x in zip(*l):
        message.append(collections.Counter(x).most_common(1)[0][0])

    return "".join(message)

def errorCorrect2(file):
    with open(file) as f:
        l = [list(x) for x in f]

    message = [];
    for x in zip(*l):
        message.append(collections.Counter(x).most_common()[-1][0])

    return "".join(message)


print("Input test: " + errorCorrect("data\inputTest.txt"))
print("Input     : " + errorCorrect("data\input.txt"))

print("Input test: " + errorCorrect2("data\inputTest.txt"))
print("Input     : " + errorCorrect2("data\input.txt"))