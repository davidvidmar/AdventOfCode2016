#
# Avent of Code 2016, Day 5
# http://adventofcode.com/2016/day/5
#

import hashlib
import sys

syms = ['\\', '|', '/', '-']

def getPassword(input, start=0):

    print ("Hacking password for '%s'\n" % input)    

    i = start
    password = ""

    for j in range(1,9):

        found = False
        print (j, " ", end="")

        while not found:
            code = input + str(i)
    
            m = hashlib.md5(bytes(code, "ascii"))
            hash = m.hexdigest()
  
            i += 1
            if (i % 10000 == 0): 
                sym = syms[int((i / 10000) % 4)]
                sys.stdout.write("\b%s" % sym)
                sys.stdout.flush()

            found = hash[:5] == '00000'
    
        print("\b%s -> %s" % (code, hash))
    
        password += hash[5]

    return password

def getPassword2(input, start=0):

    print ("Hacking password(2) for '%s'\n" % input)

    i = start
    j = 0
    password = "________"    

    while password.find("_") > -1:

        found = False
        print (j, " ", end="")

        while not found:
            code = input + str(i)
    
            m = hashlib.md5(bytes(code, "ascii"))
            hash = m.hexdigest()
  
            i += 1
            if (i % 10000 == 0): 
                sym = syms[int((i / 10000) % 4)]
                sys.stdout.write("\b%s" % sym)
                sys.stdout.flush()

            found = hash[:5] == '00000'
    
        if (hash[5].isdigit()):
            pos = int(hash[5])
            if (pos < len(password) and password[pos] == '_'):
                password = password[:pos] + hash[6] + password[pos+1:]        
                print("\b%s -> %s -> %s" % (code, hash, password))
            else:
                print("\b%s -> %s -> %s" % (code, hash, "/invalid index/"))
        else:
            print("\b%s -> %s -> %s" % (code, hash, "/not digit/"))

        j += 1

    return password

print("\nPassword = %s\n" % getPassword2("abc", 3000000))
print("\nPassword = %s\n" % getPassword2("ojvtpuvg", 146959))