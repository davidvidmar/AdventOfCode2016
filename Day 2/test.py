import day2
import part1

inputs = ("ULL", 
          "RRDDD", 
          "LURDL", 
          "UUUUD")

def Process():
    
    decoder = day2.Decoder(part1.r, part1.bounds, 1, 1)
  
    code = []

    for input in inputs:
        result = decoder.Decode(input)
        code.append(result)
    
    return code