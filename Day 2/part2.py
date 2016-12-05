import day2
import part1;

#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D

r = (0, 0, 1, 0, 0), (0, 2, 3, 4, 0), (5, 6, 7, 8, 9), ('', 'A', 'B', 'C', ''), ('', '', 'D', '', '')

lb = 2, 1, 0, 1, 2
rb = 2, 3, 4, 3, 2
tb = 2, 1, 0, 1, 2
bb = 2, 3, 4, 3, 2

bounds = lb, rb, tb, bb

def Process():

    decoder = day2.Decoder(r, bounds, 0, 2)

    code = []

    for input in part1.inputs:
        result = decoder.Decode(input)
        code.append(result)        
    
    return code
