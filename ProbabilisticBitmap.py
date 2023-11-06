import math
import random
import sys


class bitmap:

    def __init__(self,m,p):
        self.n = 5
        self.p=p
        self.m = m
        self.true = [100, 1000, 10000, 100000, 1000000]
        self.estimated_size = []
        self.arr = [0 for i in range(self.m)]
        self.elements = [0 for i in range(self.n)]

    def gen(self,n):

        self.elements=random.sample(range(0,sys.maxsize),n)


    def solve(self):
        temp=-1
        for i in self.true:
            vb.gen(i)
            
            for element in self.elements:
                temp=max(temp,hash(element))

            for element in self.elements:
                if hash(element) <temp *self.p:
                    self.arr[hash(element)%self.m]=1


                        
            u=self.arr.count(0)
            v=u/self.m
            
            if v == 0: 
                self.estimated_size.append('inf') #representing ln(0) as undefined
            else:
                log_V = math.log(v)*(1/self.p)
                estimated =  -self.m * (log_V)
                self.estimated_size.append(estimated)
            




if __name__ == '__main__':

    m = int(input("no. of bits in the bitmap: "))
    p = float(input("sampling probability: "))

    vb = bitmap(m,p)
    vb.solve()    
    doc = open("output2.txt", 'w')

    for i in range(len(vb.estimated_size)):
        print(str(vb.true[i]) + "  " + str(vb.estimated_size[i]), file=doc)








