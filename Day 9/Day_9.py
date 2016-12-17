#
# Avent of Code 2016, Day 9
# http://adventofcode.com/2016/day/9
#

inputTest = (#("(3x3)XYZ(3x3)ABC", "XYZXYZXYZABCABCABC"), 
             #("ADVENT", "ADVENT"), ("A(1x5)BC", "ABBBBBC"), 
             #("(3x3)XYZ", "XYZXYZXYZ"), ("A(2x2)BCD(2x2)EFG", "ABCBCDEFEFG"), 
             ("(6x1)(1x3)A", "(1x3)A"), 
             ("X(8x2)(3x3)ABCY", "X(3x3)ABC(3x3)ABCY"))

inputTest2 = (#("(3x3)XYZ", "XYZXYZXYZ"), 
              ("X(8x2)(3x3)ABCY", "XABCABCABCABCABCABCY"),
              #("(27x12)(20x12)(13x14)(7x10)(1x12)A", ""), ("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", "")
             )

def Decompress(s):
    
    output = ""
    
    inMarker = False;
    marker = "";
    markerLen = 0;
    markerCnt = 0;

    r = ""   
    
    for c in s:
        
        if inMarker and c == ")":
            inMarker = False
            markerLen = int(marker.split("x")[0])
            markerCnt = int(marker.split("x")[1])
        elif inMarker:
            marker += c
        elif c == "(" and marker == "":
            inMarker = True        
        elif (marker != ""):
            if len(r) < markerLen:
                r += c                        
            elif len(r) == markerLen:                
                for i in range(0, markerCnt):
                    output += r
                marker = "";
                r = "";
                if c == "(":
                    inMarker = True
                else:
                    output += c
                
            else:
                raise ValueError("bu?")
        else:
            output += c;        

    if (marker != ""):
        for i in range(0, markerCnt):
            output += r

    return output;

def Decompress2(s):
    while s.find("(") > -1:        
        s = Decompress(s)
    return s

def DecompressCount(s):
    
    inMarker = False;
    marker = "";
    markerLen = 0;
    markerCnt = 0;    
    length = 0;
    
    for i in range(len(s) - 1, 0, -1):
        c = s[i];
        
        if c == ")":
            inMarker = True
        elif inMarker and c == "(":            
            markerLen = int(marker.split("x")[0])
            markerCnt = int(marker.split("x")[1])
            inMarker = False            
            marker = ""            
            length = length - markerCnt + markerCnt * markerLen;
        elif inMarker:
            marker += c                      
        else:            
            length += 1;

    if inMarker:            
        markerLen = int(marker.split("x")[0])
        markerCnt = int(marker.split("x")[1])        
        length = length - markerCnt + markerCnt * markerLen;
    else:
        length += 1;

    return length;


#print("Test: ")
#for t in inputTest:
    #print("%s: %s = %s = %s (%d)" % (t[0], t[1], Decompress(t[0]), str(Decompress(t[0]) == t[1]), len(Decompress(t[0]))))    
#print("")

for t in inputTest2:
    print("%s: %s = %s = %s (%d)" % (t[0], t[1], "", str(Decompress2(t[0]) == t[1]), len(Decompress2(t[0]))))
    print("Dlen", DecompressCount(t[0]))
print(".")

exit()

print("Input:")
with open("data\input.txt") as f:
    for line in f:
        line = line.strip()
        s = Decompress(line)
        #print(s)
        print(len(s))

print("Input 2:")
with open("data\input.txt") as f:
    for line in f:
        line = line.strip()
        s = Decompress2(line)
        #print(s)
        print("final: ", len(s))