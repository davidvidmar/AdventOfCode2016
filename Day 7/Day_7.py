#
# Avent of Code 2016, Day 7
# http://adventofcode.com/2016/day/7
#

inputTestTLS = ("abba[mnop]qrst", "abcd[bddb]xyyx", "aaaa[qwer]tyui", "ioxxoj[asdfgh]zxcvbn")
inputTestSSL = ("aba[bab]xyz", "xyx[xyx]xyx", "aaa[kek]eke", "zazbz[bzb]cdb")

def checkTLS(line):
    valid = False
    while line.find('[') > -1:
        part1 = line[:line.index('[')]
        middle = line[line.index('[')+1:line.index(']')]    
        line = line[line.index(']')+1:]
        valid = valid or checkABBA(part1)
        if checkABBA(middle):
            return False
    return valid or checkABBA(line)
    
def checkABBA(ip):
    
    if len(ip) < 4:
        return False

    i = 0
    while i <= len(ip) - 4:
        if ip[i] == ip[i+3] and ip[i+1] == ip[i+2] and ip[i] != ip[i+1]:
            return True
        i += 1

    return False

def checkSSL(line):    
    supernet = []
    hypernet = []
    while line.find('[') > -1:
        supernet.append(line[:line.index('[')])
        hypernet.append(line[line.index('[')+1:line.index(']')])
        line = line[line.index(']')+1:]        
    supernet.append(line)
    return checkABA(supernet, hypernet)

def checkABA(supernet, hypernet):    
    result = False
    for ip in supernet:
        i = 0
        while i <= len(ip) - 3:
            if ip[i] == ip[i+2] and ip[i] != ip[i+1]:
                if checkBAB(ip[i:i+3], hypernet): 
                    return True
            i += 1
    return result

def checkBAB(aba, hypernet):
    if len(aba) != 3:
        raise ValueError("invalid length")
    
    bab = aba[1] + aba[0] + aba[1]

    for ip in hypernet:
        if ip.find(bab) > -1:
            return True

    return False

# test
print("Test TLS:")
for line in inputTestTLS:
    print(line + " -> " + str(checkTLS(line)))
print()

print("Test SSL:")
for line in inputTestSSL:
    print(line + " -> " + str(checkSSL(line)))
print()


print("Input:")

# puzzle 1
with open("data\input.txt") as f:
    countTLS = 0
    countSSL = 0

    for line in f:        
        if checkTLS(line): countTLS += 1
        if checkSSL(line): countSSL += 1
    
print("Lines with TLS: " + str(countTLS))
print("Lines with SSL: " + str(countSSL))