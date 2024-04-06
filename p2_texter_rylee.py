# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:08:08 2024

@author: rylee
"""

import random
from itertools import filterfalse, islice
from functools import reduce

##code from problem one
def rnd_gen(x0, n):
    count = 0
    while True:
        if n >= 0 and count >= n:
            break
        else:
            x0 = random.randint(0, 1000) * x0 % 65537
            yield x0
            count += 1
#part a
def gen_rndtup(m):
    itera = rnd_gen(1, -1)
    while True:
        a = next(itera) % m
        b = next(itera) % m
        if a <= b:
            yield (a, b)
  
#part b
generator = gen_rndtup(10)
tups = filterfalse(lambda x: x[0] + x[1] < 6, islice(generator, 8))
print("part b")
for tup in tups:
    print(tup)
    
#part c
gen_a = (x % 101 for x in rnd_gen(1, -1))
gen_b = (x % 101 for x in rnd_gen(2, -1))

#combines a and b into a tuple
ab = zip(gen_a, gen_b)
tups1 = ((a, b) for a, b in ab if a <= b)

print()
print("part c")
count = 0
for tup in tups1:
    print(tup)
    if count == 7:
        break;
    count +=1
    
    
#part d
generator = rnd_gen(1, -1)

numbers = filter(lambda x: x % 13 == 0, map(lambda x: x % 101, generator))
firstten = list(islice(numbers, 10))
print()
print("part d")
print(firstten)


#part e
generator1 = gen_rndtup(10)

tups2=  filter(lambda tup: sum(tup) >= 5, generator1)
tentups = islice(tups2, 10)


total = reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), tentups)
print()
print("part e")
print(total)


