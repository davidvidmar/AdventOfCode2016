import collections
import re
from operator import itemgetter
from string import ascii_lowercase as alphabet
        
rooms = open("data\input.txt", "r") 

def checkName(room):

    #aaaaa-bbb-z-y-x-123[abxyz]

    nameId, checkSum = room.split("[")

    name = re.sub('[^a-z]', '', nameId)
    sectorId = re.sub('[^0-9]', '', nameId)
    checkSum = re.sub('[^a-z]', '', checkSum)    

    counter = collections.Counter(name)

    sorted1 = sorted(counter.items(), key=itemgetter(0))
    sorted2 = sorted(sorted1, reverse=True, key=itemgetter(1))
    realCheckSum = "".join([x for x,_ in sorted2][:5])

    #print(checkSum, "=", realCheckSum)       

    if checkSum == realCheckSum:
        shift = int(sectorId) % 26
        cipher = str.maketrans(alphabet, alphabet[shift:] + alphabet[:shift])
        
        decoded = re.sub('[^a-z]', ' ', nameId).translate(cipher)

        if decoded.find('north') > -1:
            print(decoded)
            print(sectorId)
        
        return int(sectorId)
    else:
        return 0

print(checkName("aaaaa-bbb-z-y-x-123[abxyz]") +
    checkName("a-b-c-d-e-f-g-h-987[abcde]") +
    checkName("not-a-real-room-404[oarel]") +
    checkName("totally-real-room-200[decoy]"))

sectorIdSum = 0;
for room in rooms:    
    sectorIdSum += checkName(room)    
    
print(sectorIdSum)