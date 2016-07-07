#!/usr/bin/env python 2
import math
import sys
from common import print_solution,read_input
import random

def distance(city1,city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    # Build a trivial solution.
    # Visit the cities in the order they appear in the input.
    return list(range(len(cities)))
cities=read_input(sys.argv[1])
n=len(cities)-1
m=1
dis=0


while 1 :
    if m<=n:
        dis += distance(cities[m-1],cities[m])
        m+=1
    else:
        break



total_dis=dis+distance(cities[0],cities[n])
print total_dis


while True:
    cities=read_input(sys.argv[1])
    random.shuffle(cities)
    n2=len(cities)-1
    mm=1
    sdis=0
    while 1 :
        if mm<=n2:
            sdis += distance(cities[mm-1],cities[mm])
            mm+=1
        else:
            break
    short_dis=sdis+distance(cities[0],cities[n])

        if short_dis>total_dis:
            total_dis=short_dis
        continue
    else:
        break
print short_dis

























      