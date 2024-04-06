# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:19:33 2024

@author: rylee
"""
import random

class RndSeq:
    #initiallizes seed, cound and n
    def __init__(self, x0, n):
        self.seed = x0
        self.count = 0
        self.n = n

    ##returns the current iteration
    def __iter__(self):
        return self

    #returns the next iteration and keeps track, raises StopIteration
    #if reached the end
    def __next__(self):
        if self.n >= 0 and self.count >= self.n:
            raise StopIteration
            
        else:
            self.count += 1
            self.seed = random.randint(0, 1000) * self.seed % 65537
            return self.seed
        
#generates n  random numbers using seed of x0
def rnd_gen(x0, n):
    count = 0
    #breaks when 
    while True:
        if n >= 0 and count >= n:
            break
        else:
            x0 = random.randint(0, 1000) * x0 % 65537
            yield x0
            count += 1

def main():
    
    rnd = RndSeq(1, 10)
    
    print("ten random numbers")
    for num in rnd:
        print(num)
    print()
    
    rnd2 = RndSeq(1, 2)
    it = iter(rnd2)
    print("next iteration")
    print(next(it))
    print("next iteration")
    print(next(it))
    # print(next(it))
    
    print()
    print([i for i in rnd_gen(1, 10)])
    print(list(rnd_gen(1, 3)))

main()
