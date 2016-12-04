# day 2, decoder

class Decoder:

    def __init__(self, resultTable, bounds, startX, startY):

        self.r = resultTable
     
        self.lb = bounds[0]
        self.rb = bounds[1]
        self.tb = bounds[2]
        self.bb = bounds[3]

        self.x = startX
        self.y = startY
    
    def Decode(self, input):

        print(self.r[self.y][self.x])

        for c in input:
            if (c == 'U'):
                if (self.y > self.tb[self.x]): self.y = self.y - 1;
            elif (c == 'D'):
                if (self.y < self.bb[self.x]): self.y = self.y + 1;
            elif (c == 'L'):
                if (self.x > self.lb[self.y]): self.x = self.x - 1;
            elif (c == 'R'):
                if (self.x < self.rb[self.y]): self.x = self.x + 1;
            print(c, self.r[self.y][self.x])        

        return self.r[self.y][self.x]
