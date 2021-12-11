import copy
from os import curdir
from util import sort_and_remove_dup

def solve(input):
    ansA = None
    ansB = None

    normalized_input = normalize_input(input)

    ansA = shortest_distance(normalized_input, False)
    ansB = shortest_distance(normalized_input, True)
    return ansA, ansB

def normalize_input(input):
    output = []

    split_input = input[0].split(',')

    for entry in split_input:
        output.append(int(entry))

    return output

def shortest_horizontal(input):
    output = 0
    
    # Cut the list down to a lower 1/3rd of elements.
    consec_list = [*range(0, max(input)+1, 1)]

    least_fuel = 2**64
    current_fuel = 0

    for candidate in consec_list:
        for dist in input:
            current_fuel += (abs(candidate - dist))

        if(current_fuel < least_fuel):
            least_fuel = current_fuel
            
        current_fuel = 0            

    return least_fuel

def shortest_distance(input, compound):
    output = 0

    # Sort and remove duplicates.
    sort_input = copy.deepcopy(input)
    sort_input.sort()
    sort_input = list(dict.fromkeys(sort_input))
    
    # Cut the list down to a lower 1/3rd of elements.
    cut_rate = int(len(sort_input)* (1/1))
    consec_list = [*range(0, max(input)+1, 1)]

    least_fuel = 2**64
    current_fuel = 0

    for candidate in consec_list:
        for dist in input:
            distance = abs(candidate - dist)
            if compound:
                distance = summation(distance)
            current_fuel += distance

        if(current_fuel < least_fuel):
            least_fuel = current_fuel
            
        current_fuel = 0

    return least_fuel

def summation(num):
    
    if num <= 0:
        return 0
      
    output = 0

    for i in range(num):
        output += (num - i)
    
    return output