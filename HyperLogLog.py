import sys
from functools import reduce
import random
import uuid

class HLL:

    def __init__(self,m):
        self.n = 5
        self.m = 256
        self.bits=32
        self.true = [1000, 10000, 100000, 1000000]
        self.arr = [0 for i in range(self.m)]
        self.estimated_size={}
        self.flow_ids = []
           
    def gen(self):

        for i in self.true:
            self.s=random.sample(range(0,sys.maxsize),i)       
            self.flow_ids.append(self.s)
    
    def check(self):
        
        self.gen()
        self.solve()
        

    def reset(self):
        x=0
        while(x<len(self.arr)):
            self.arr[x] = 0
            x=x+1
    
    def zero(self, value):
        
        val = 0
        while ((value & (1 << (self.bits - 1))) == 0):
            value = (value << 1)
            val = val + 1
        return val

    def solve(self):
        rand_hash = uuid.uuid4().int
        f=0
        while(f<len(self.true)):

            rid = self.flow_ids[f]
            
            for value in rid:
                l=[value,rand_hash]
                res = reduce(lambda x, y: x ^ y, l)
                hash_val=self.zero(value) + 1
                res = res % self.m
                self.arr[res] = max(self.arr[res],hash_val)
            
            a = 0.7213/(1+(1.079 / self.m))
            temp = 0
            i=0

            while(i<len(self.arr)):
                add= 2 ** self.arr[i]
                temp = temp + (1 / add)
                i=i+1
            temp = (1 / temp) * (a * (self.m ** 2))
            self.estimated_size[f] = temp
            self.reset()
            f=f+1


if __name__ == '__main__':

    m = int(input("no. of registers: "))

    vb = HLL(m)
    vb.check()    
    doc = open("output3.txt", 'w')

    for i in range(len(vb.estimated_size)):
        print(str(int(vb.true[i])) + " : " + str(int(vb.estimated_size[i])) + "\n",file=doc)
        