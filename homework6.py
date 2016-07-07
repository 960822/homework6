#!/usr/bin/env python2

import sys
import math

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
    
def solve(cities):
    N = len(cities)
    current_city1=None
    current_city2=None
    current_city3=None
    current_city4=None
    m=-100000000
    n=100000000

    for city in cities:
        if m < city[0]+city[1]:
            current_city3 =city
        if n > city[0] + city[1]:
            current_city2 = city
        if m < city[1]-city[0]:
            current_city4= city
        if n > city[1]-city[0]:
            current_city1=city
    cities.extend(current_city1)
    cities.extend(current_city2)
    cities.extend(current_city3)
    cities.extend(current_city4)
    
    h=(current_city1[1]-current_city3[1])/2
    w=(current_city4[0]-current_city3[0])/2
    offset = (h,w)

    def distance_from_current_city1(city):
        return distance(current_city1, cities[city])
    def distance_from_current_city2(to):
        return distance(current_city2, cities[city])
    def distance_from_current_city3(to):
        return distance(current_city3, cities[city])
    def distance_from_current_city4(to):
        return distance(current_city4, cities[city])

    last_city=0
    sum1=0
    unvisited_cities = set(range(1, N))
    solution = [current_city1]

    while unvisited_cities:
        next_city1 = min(unvisited_cities, key=distance_from_current_city1)#next_city は数字だからどうやってoffsetと比較する方がいいですか
        if  next_city1[0]>= offset[0] and next_city1[1]>=offset[1]:
            sum1 += distance(current_city1,next_city1)
            unvisited_cities.remove(next_city1)
            solution.append(next_city1)
            current_city1 = next_city1
            sum1 += distance(current_city1,next_city1)
        else:
            break
    return solution
    return sum1

    last_city=0
    sum2=sum1
    solution = [current_city2]

    
    while unvisited_cities:
        next_city2 = min(unvisited_cities, key=distance_from_current_city2)
        if next_city2[0]>= offset[0] and next_city2[1]>=offset[1]:
            sum += distance(current_city2,next_city2)
            unvisited_cities.remove(next_city2)
            solution.append(next_city2)
            current_city2 = next_city2
            sum2 +=distance(current_city2,next_city2)
        else:
            break
    

    return solution
    return sum2
    
    last_city=0
    sum3=sum2
    solution=[current_city3]

    while unvisited_cities:
        next_city3 = min(unvisited_cities, key=distance_from_current_city3)
        if next_city3[0]<= offset[0] and next_city3[1]<= offset[1]:
            sum += distance(current_city3,next_city3)
            unvisited_cities.remove(next_city3)
            solution.append(next_city3)
            current_city3 = next_city3
            sum3 += distance(current_city3,next_city3)
        else:
            break
    
    return solution
    return sum3

    last_city=0
    sum4=sum3
    solution = [current_city4]

    while unvisited_cities:
    
        next_city4 = min(unvisited_cities, key=distance_from_current_city4)
        if nex_city4[0]<= offset[0] and next_city4[1]>= offset[1]:
        
            sum += distance(current_city4,next_city4)
            unvisited_cities.remove(next_city4)
            solution.append(next_city4)
            current_city4 = next_city4
            sum4 += distance(current_city4,next_city4)
            sum5 = sum4+distance(current_city1,current_city2)+distance(current_city2,current_city3)+distance(current_city3,current_city4)+distance(current_city4,current_city1)
    print sum5
    



    
    
  

if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)


        
